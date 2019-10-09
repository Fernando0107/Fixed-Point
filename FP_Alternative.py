from scipy import optimize
import numpy as np


def func(x, c1, c2):
    z = np.sqrt(c1/(x+c2))
    return z

c1 = np.array([10, 12.])
c2 = np.array([3, 5.])

print("\nFixed Point: \n",optimize.fixed_point(func, [1.2, 1.3], args=(c1, c2)),'\n')
