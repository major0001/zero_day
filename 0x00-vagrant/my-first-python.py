#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plt
import scipy
%matplotlib inline
x= np.linspace(0,3,200)
y =x*3
plt.plot(x,y,"-g",lable="plot of x against y")
