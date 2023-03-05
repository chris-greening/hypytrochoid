import math

import numpy as np
import matplotlib.pyplot as plt

from hypytrochoid import Hypotrochoid

R = 200
r = 122.5
d = 300
thetas = np.arange(0,360, .005)

hypotrochoid = Hypotrochoid(R, r, d, thetas)

plt.plot(hypotrochoid.x, hypotrochoid.y, linewidth=.2)
plt.show()
