import control as ctrl
import numpy as np
from plotting import Plotter

class Analysis:

	@staticmethod
	def time (tf, method = 'step', plot = False):
	    print "==================================================================";
	    print "Poles:   ", ctrl.pole (tf);
            print "Zeros:   ", ctrl.zero (tf);
	    dc = ctrl.dcgain (tf);

	    print "DC gain: ", dc;
	    if (method == 'step'):
	       t, y = ctrl.step_response (tf);
	    if (method == 'impulse'):
	       t, y = ctrl.impulse_response (tf);
 
	    ys = filter (lambda l: l >= 0.98 * dc, y);
            i = np.ndarray.tolist(y).index (min (ys));
            print "Ts: ", t[i];
	    print "Overshoot: ", (max (y) / dc) - 1;	
	    i = np.ndarray.tolist(y).index (max (y));
	    print "Tr: ", t[i];
	
	    if (plot == True):
		p = Plotter ({'grid' : True});
		p.plot ([(t, y)]);

            return t, y

	@staticmethod
	def bode (tf, plot = False):
	    print "==================================================================";
            gm, pm, wg, wp = ctrl.margin (tf);
	    print "Gain Margin: ", gm, " dB in ", wg, " rad/s"; #Verificar informacoes
	    print "Phase Margin: ", gm, "deg in", wp, " rad/s";
	    mag, pha, w = ctrl.bode_plot (tf);
	    if (plot == True):
	       p = Plotter ({'type' : 'log', 'grid' : True});
	       p.subplot ([(w, 20*np.log10(mag)), (w, (180*pha/np.pi))], ["Gain (dB)", "Phase (deg)"]);
	
	    return gm, pm, wg, wp
