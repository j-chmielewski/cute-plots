#!/bin/env python

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy import arange, sin, cos, pi, ones, linspace, log

fig = plt.figure()
x = arange(0, 10*pi, .1)

plt.plot(x, x**2*sin(x), x, 2*x*sin(x) + x**2*cos(x), x, [0] * len(x), 'r--')

plt.xlabel('X')
plt.ylabel('Y')
plt.legend(["x^2sin(x)", "2xsin(x)+x^2cos(x)"])
plt.show()
