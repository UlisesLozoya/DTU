"""Problems for the Bisection project in week 3."""
import math


def f(x: float) -> float:
    r"""Find the roots of this function.

    You should implement the function :math:`f(x)` here. It is defined as:

    . math::

        f(x) = \sin(3\cos(\frac{1}{2} x^2))

    :param x: The value to evaluate the function in :math:`x`
    :return: :math:`f(x)`.
    """
    # Compute f(x) here.
    # TODO: Code has been removed from here.
    k = math.sin(3 * math.cos((1 / 2) * x**2))
    return k


def is_there_a_root(a: float, b: float) -> bool:
    """Return ``True`` if we are guaranteed there is a root of ``f`` in the interval :math:`[a, b]`.

    :param a: Lowest x-value to consider
    :param b: Highest x-value to consider
    :return: ``True`` if we are guaranteed there is a root otherwise ``False``.
    """
    # TODO: Code has been removed from here.
    x1 = f(a)
    x2 = f(b)
    if x1 == 0 or x2 == 0:
        return True
    if x1 < 0 < x2 or x2 < 0 < x1:
        return True
    else:
        return False


def bisect(xmin: float, xmax: float, delta: float) -> float:
    """Find a candidate root within ``xmin`` and ``xmax`` within the given tolerance.

    :param xmin: The minimum x-value to consider
    :param xmax: The maximum x-value to consider
    :param delta: The tolerance.
    :return: The first value :math:`x` which is within ``delta`` distance of a root according to the bisection algorithm
    """
    # TODO: Code has been removed from here.
    xmid = (xmin + xmax) / 2
    if not is_there_a_root(xmin, xmax):
        return math.nan
    while not xmax - xmin <= 2 * delta:
        rootleft = is_there_a_root(xmin, xmid)
        rootright = is_there_a_root(xmid, xmax)
        if rootleft:
            xmax = xmid
            xmid = (xmin + xmax) / 2
            continue
        elif rootright:
            xmin = xmid
            xmid = (xmin + xmax) / 2
            continue
        elif f(xmax) == 0:
            return xmax
        elif f(xmin) == 0:
            return xmin
        elif xmax - xmin <= 2 * delta:
            return xmid
        elif not rootright and not rootleft:
            return math.nan
    else:
        return xmid


if __name__ == "__main__":
    t = 1
    y = 3
    z = 0.001
    print(bisect(t, y, z))
