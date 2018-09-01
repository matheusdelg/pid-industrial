import control as ctrl
import numpy as np
from utils import insert


class Controller:

    specs = None;
    tf = None;

    def __init__ (self, specs = None):
	self.specs = specs;
	self.instantiate ();

    def instantiate (self, specs = None):

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
	else:
	   Ci = 0;

	if (self.Td != 0):
	   num_d = [self.Kc * self.Td * self.c, 0];
           den_d = [(self.Td / self.N), 0];
	   Cd = ctrl.tf (num_d, den_d);
	else:
	   Cd = 0;

        self.tf = Cp + Ci + Cd;
