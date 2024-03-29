from scipy import optimize
import numpy as np
from scipy._lib._util import _asarray_validated, _lazywhere


def _del2(p0, p1, d):
    return p0 - np.square(p1 - p0) / d


def _relerr(actual, desired):
    return (actual - desired) / desired


def _fixed_point_helper(func, x0, args, xtol, maxiter, use_accel):
    p0 = x0
    for i in range(maxiter):
        p1 = func(p0, *args)
        if use_accel:
            p2 = func(p1, *args)
            d = p2 - 2.0 * p1 + p0
            p = _lazywhere(d != 0, (p0, p1, d), f=_del2, fillvalue=p2)
        else:
            p = p1
        relerr = _lazywhere(p0 != 0, (p, p0), f=_relerr, fillvalue=p)
        if np.all(np.abs(relerr) < xtol):
            return p
        p0 = p
    msg = "Failed to converge after %d iterations, value is %s" % (maxiter, p)
    raise RuntimeError(msg)


def fixed_point(func, x0, args=(), xtol=1e-8, maxiter=500, method='iteration'):
    """
    Find a fixed point of the function.
    Given a function of one or more variables and a starting point, find a
    fixed-point of the function: i.e. where ``func(x0) == x0``.
    Parameters
    ----------
    func : function
        Function to evaluate.
    x0 : array_like
        Fixed point of function.
    args : tuple, optional
        Extra arguments to `func`.
    xtol : float, optional
        Convergence tolerance, defaults to 1e-08.
    maxiter : int, optional
        Maximum number of iterations, defaults to 500.
    method : {"del2", "iteration"}, optional
        Method of finding the fixed-point, defaults to "del2"
        which uses Steffensen's Method with Aitken's ``Del^2``
        convergence acceleration [1]_. The "iteration" method simply iterates
        the function until convergence is detected, without attempting to
        accelerate the convergence.
    References
    ----------
    .. [1] Burden, Faires, "Numerical Analysis", 5th edition, pg. 80
    Examples
    --------
    """
    use_accel = {'del2': True, 'iteration': True}[method]
    x0 = _asarray_validated(x0, as_inexact=True)
    
    return _fixed_point_helper(func, x0, args, xtol, maxiter, use_accel)

def func(x,c1,c2):

    z = np.sqrt(c1/(x+c2))

    return z


c1 = np.array([10, 12, 34, 70])
c2 = np.array([3, 5, 70, 80])

print("Result: \n",fixed_point(func, [10, 20, 20, 15], args=(c1, c2)))
