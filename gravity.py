#!/bin/env python

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy import arange, sin, cos, pi, ones, linspace

fig = plt.figure()
r = arange(0.1, 1, .01)

# assume fixed m1*m2
m1m2 = 10
# gravitational constant
G = 6.67384e-11

plt.plot(r, G * m1m2 / r**2, r, -2*G * m1m2 / r**3)

plt.xlabel('r')
plt.ylabel('gravity')
plt.legend(["gravity", "d gravity/dr"], loc="lower right")
plt.show()
