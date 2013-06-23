#!/bin/env python

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy import arange, sin, cos, pi, ones, linspace, log, sqrt
from scipy.constants import c

fig = plt.figure()
ax = fig.add_subplot(111)
v = linspace(0, 1, 500)

ax.yaxis.set_ticks(range(0, 16))
ax.grid(True)
ax.plot(v, 1./sqrt(1 - (v*c/c)**2))

plt.xlabel('V/C')
plt.ylabel('Lorenz Factor')
plt.show()
