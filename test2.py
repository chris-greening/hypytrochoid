import numpy as np

from hypytrochoid import Hypotrochoid

R = 200
d = 300
thetas = np.arange(0,360, .2)
r = 142

hypotrochoid = Hypotrochoid(R, r, d, thetas)
hypotrochoid.trace(exit_on_click=True, speed = 1)

