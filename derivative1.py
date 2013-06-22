#!/bin/env python

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy import arange, sin, cos, pi, ones, linspace

fig = plt.figure()
x = arange(0, 10*pi, .1)

plt.plot(x, sin(x), x, cos(x))
for p in arange(0, 10*pi, pi/2):
    plt.plot(ones(10)*p, linspace(-2, 2, 10), 'r--')

plt.xlabel('X')
plt.ylabel('Y')
plt.legend(["sin(x)", "sin'(x)"])
plt.show()
