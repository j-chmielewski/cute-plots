#!/bin/env python

import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from numpy import arange, sin, cos, meshgrid, sqrt, log

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

r = arange(-10, 10, .1)
X, Y = meshgrid(r, r)

Z = -X**2 - Y**2

ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')

ax.contour(X, Y, Z, extend3d=True, cmap=cm.summer)
plt.show()
