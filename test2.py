import math

import numpy as np
import matplotlib.pyplot as plt

from hypotrochoid import Hypotrochoid

R = 200
r = 122.5
d = 300
thetas = np.arange(0,360, .005)

test_hypotrochoid = Hypotrochoid(R, r, d, thetas)

plt.plot(test_hypotrochoid.x, test_hypotrochoid.y, linewidth=.2)
plt.show()
