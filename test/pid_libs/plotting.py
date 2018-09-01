import numpy as np
import matplotlib.pyplot as plt
from utils import insert

class Plotter:    

    def __init__ (self, specs = None):
	self.title = insert ("Standard Plot", specs, 'title');
	self.xlab  = insert ("Time (s)", specs, 'xlab');
	self.ylab  = insert ("Signal", specs, 'ylab');
	self.grid  = insert (False, specs, 'grid');
	self.type  = insert ("linear", specs, 'type');

    def plot (self, results, legends = None):

	for (x, y) in results:
	    if (self.type == "linear"):
		plt.plot (x, y);
	    if (self.type == "log"):
		plt.semilogx (x, y);

        if (legends is not None):
            plt.legend (legends);

	if (self.grid == True):
	   plt.grid ();

	plt.title (self.title);
	plt.xlabel (self.xlab);
	plt.ylabel (self.ylab);
        plt.show ();

    def subplot (self, results, title = None):
        n = len (results);
	nx = np.ceil(np.sqrt(n))
	ny = np.ceil (n / nx);
        i = 1

	for (x, y) in results:
	    plt.subplot (nx, ny, i);
 	    if (title is not None):
		plt.title (title[i - 1]);
	    if (self.grid == True):
	        plt.grid ();
	    if (self.type == "linear"):
		plt.plot (x, y);
	    if (self.type == "log"):
		plt.semilogx (x, y);
            i = i + 1;
	plt.show ();
