"""Exercise 3.10: Ackermann's function."""
import math


def ackermann(m: int, n: int):
    """Compute the Ackermann's function :math:`A(m, n)`.

    Your implementation should use recursion and not loops.

    :param m: the variable m.
    :param n: the variable n.
    :return: the computed value :math:`A(m,n)`.
    """
    a = 0
    # TODO: Code has been removed from here.
    if m == 0:
        a = n + 1
        return a
    if m > 0 and n == 0:
        a = ackermann(m - 1, 1)
        return a
    if m > 0 and n > 0:
        k = ackermann(m, n - 1)
        a = ackermann(m - 1, k)
        return a


if __name__ == "__main__":
    x = int(input("Enter the m value: "))
    y = int(input("Enter the n value: "))
    print(ackermann(x, y))
