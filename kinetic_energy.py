#!/bin/env python

import matplotlib.pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D
from numpy import arange, sin, cos, meshgrid, sqrt, log

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

r = arange(-10, 10, .1)
m, v = meshgrid(arange(0, 50, .1), arange(0, 30, .1))

e = (m * v**2) / 2

ax.set_xlabel('m')
ax.set_ylabel('v')
ax.set_zlabel('e')

surf = ax.plot_surface(m, v, e, alpha=.75, cmap=cm.summer)
fig.colorbar(surf, shrink=.75)
plt.show()
