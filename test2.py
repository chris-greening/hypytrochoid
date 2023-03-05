import math

import numpy as np
import matplotlib.pyplot as plt

R = 200
r = 122.5
d = 300

class Hypotrochoid:
    """Model of a hypotrochoid"""
    def __init__(self, R, r, d, thetas) -> None:
        self.R = R
        self.r = r
        self.d = d
        self.thetas = thetas 
    
        self.x = [calculate_x(R, r, d, theta) for theta in self.thetas]
        self.y = [calculate_y(R, r, d, theta) for theta in self.thetas]

def calculate_x(R: float, r: float, d: flaot, theta: float) -> float:
    """Return calculated x-value from parametrized equation"""
    return (R - r)*math.cos(theta) + d*math.cos(((R-r)/r)*theta)

def calculate_y(R: float, r: float, d: flaot, theta: float) -> float:
    """Return calculated y-value from parametrized equation"""
    return (R - r)*math.sin(theta) + d*math.sin(((R-r)/r)*theta)

# Vectorize equations 
vx = np.vectorize(x)
vy = np.vectorize(y)

thetas = np.arange(0,360, .005)
x_vals = vx(thetas)
y_vals = vy(thetas)
plt.plot(x_vals, y_vals, linewidth=.2)
plt.show()
