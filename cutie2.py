#!/bin/env python

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy import arange, sin, cos

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

r = arange(-40, 40, .1)
print len(r)
for i in range(0, 10):
    ax.scatter(r, i*r**2*sin(r), i*r**2*cos(r))
plt.show()
