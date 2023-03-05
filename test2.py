import math

import numpy as np
import matplotlib.pyplot as plt

R = 200
r = 122.5
d = 300

def x(theta: int) -> int:
    """Return calculated value of parametrized x equation"""
    return (R - r)*math.cos(theta) + d*math.cos(((R-r)/r)*theta)

def y(theta: int) -> int:
    """Return calculated value of parametrized x equation"""
    return (R - r)*math.sin(theta) + d*math.sin(((R-r)/r)*theta)

# Vectorize equations 
vx = np.vectorize(x)
vy = np.vectorize(y)

thetas = np.arange(0,360, .005)
x_vals = vx(thetas)
y_vals = vy(thetas)
plt.plot(x_vals, y_vals, linewidth=.2)
plt.show()
