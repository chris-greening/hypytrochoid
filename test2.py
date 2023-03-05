import math

import numpy as np
import matplotlib.pyplot as plt

from hypytrochoid import Hypotrochoid

R = 200
d = 300
thetas = np.arange(0,360, .005)

for i, r in enumerate(np.arange(142, 143.2, .005)):
    r = round(r, 3)
    hypotrochoid = Hypotrochoid(R, r, d, thetas)
    plt.clf()
    plt.plot(hypotrochoid.x, hypotrochoid.y, linewidth=.2)
    plt.savefig(f"test/test{i}.png")