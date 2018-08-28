import matplotlib.pyplot as plt
import control as ctrl
import numpy as np

def insert (value, specs, key):
    if specs.has_key (key):
       return specs [key]
    else:
       return value

class Plotter:    

    def __init__ (self, specs):
        # Configuracoes padrao do plot:
	self.title = insert ("Standard Plot", specs, 'title');
	self.xlab  = insert ("Time (s)", specs, 'xlab');
	self.ylab  = insert ("Signal", specs, 'ylab');
	self.grid  = insert (False, specs, 'grid');

    def plot (self, results, legends = None):
	for (x, y) in results:
	    plt.plot (x, y);

        if (legends is not None):
            plt.legend (legends);

	if (self.grid == True):
	   plt.grid ();

	plt.title (self.title);
	plt.xlabel (self.xlab);
	plt.ylabel (self.ylab);
        plt.show ();

class Controller:

    specs = None;
    tf = None;

    def __init__ (self, specs):
	self.specs = specs;
	self.instantiate ();

    def instantiate (self, specs = None):

	# Sobrepor a anterior:
	if specs is not None:
	   self.specs = specs;

	self.Kc = insert (1,      self.specs, 'Kc');
        self.Ti = insert (np.inf, self.specs, 'Ti'); 
	self.Td = insert (0,      self.specs, 'Td');

	self.b  = insert (1.0, self.specs, 'b');
	self.c  = insert (1.0, self.specs, 'c');
	self.N  = insert (9.0, self.specs, 'N');

	num_p = self.Kc * self.b;
        den_p = 1;
	Cp = ctrl.tf (num_p, den_p);

	if (self.Ti != np.inf):
	   num_i = self.Kc;
	   den_i = [self.Ti, 0];
	   Ci = ctrl.tf (num_i, den_i);

	if (self.Td != 0):
	   num_d = [self.Kc * self.Td * self.c, 0];
           den_d = [(self.Td / self.N), 0];
	   Cd = ctrl.tf (num_d, den_d);

        self.tf = ctrl.parallel (Cp, 
				 Ci if 'Ci' in locals() else 0,
				 Cd if 'Cd' in locals() else 0); 

class Analysis:

	@staticmethod
	def time (tf):
	    print "Poles:   ", ctrl.pole (tf);
            print "Zeros:   ", ctrl.zero (tf);
	    dc = ctrl.dcgain (tf);
	    print "DC gain: ", dc
	    t, y = ctrl.step_response (tf);
	    ys = filter (lambda l: l >= 0.98 * dc, y);
            i = np.ndarray.tolist(y).index (min (ys));
            print "Ts: ", t[i];
	    print "Overshoot: ", (max (y) / dc) - 1;	
	    i = np.ndarray.tolist(y).index (max (y));
	    print "Tr: ", t[i];
