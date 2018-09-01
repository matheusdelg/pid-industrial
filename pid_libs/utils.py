import matplotlib.pyplot as plt
import control as ctrl
import numpy as np

def insert (value, specs, key):
    if specs is None:
	return value
    if specs.has_key (key):
       return specs [key]
    else:
       return value				 
				  
