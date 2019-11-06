#Libreriasa necesarias
from scipy import optimize
import numpy as np
from scipy._lib._util import _asarray_validated, _lazywhere


def sp_helper(actual, desired):
    return (actual - desired) / desired

def fixedPoint(function, guess, args, tol, maxit):
    p0 = guess 
    for i in range(maxit):

        p1 = function(p0, *args)

        p=p1

        relerr = _lazywhere(p0 != 0, (p, p0), f=sp_helper, fillvalue=p)
        if(np.all(np.abs(relerr) < tol)):
            return p

        p0 = p

    msg = "Failed to converge after %d iterations, value is %s" % (maxit, p)
    raise RuntimeError(msg)


def auxFixedPoint(function, guess, maxit, tol, args=()):

    guess = _asarray_validated(guess, as_inexact=True)

    return fixedPoint(function, guess, args, tol, maxit)

def function(x,c1,c2):
    
    z = np.sqrt(c1/(x+c2))

    return z


c1 = np.array([1, 12])
c2 = np.array([1, 5])

print("Result: \n", auxFixedPoint(function, [10, 20],500, 1e-8, args=(c1, c2)), "\n")

