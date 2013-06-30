#!/bin/env python

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from numpy import arange, sin, cos
import ephem
import datetime
from datetime import timedelta

# planet vectors
startDate = datetime.date(2000, 1, 1)
step = 1  # in days
r = range(0, 365 * 20)

mercury = []
venus = []
# earth = [] # no earth in pyephem - wtf...
mars = []
jupiter = []
saturn = []
uranus = []
neptune = []

for i in r:
    mercury.append(ephem.Mercury(startDate + timedelta(days=step * i)).sun_distance)
    venus.append(ephem.Venus(startDate + timedelta(days=step * i)).sun_distance)
    mars.append(ephem.Mars(startDate + timedelta(days=step * i)).sun_distance)
    jupiter.append(ephem.Jupiter(startDate + timedelta(days=step * i)).sun_distance)
    saturn.append(ephem.Saturn(startDate + timedelta(days=step * i)).sun_distance)
    uranus.append(ephem.Uranus(startDate + timedelta(days=step * i)).sun_distance)
    neptune.append(ephem.Neptune(startDate + timedelta(days=step * i)).sun_distance)

plt.plot(r, mercury, r, venus, r, mars, r, jupiter, r, saturn, r, uranus, r, neptune)

plt.legend(['mercury', 'venus', 'mars', 'jupiter', 'saturn', 'uranus', 'neptune'])
plt.title('distance from the sun')
plt.show()
