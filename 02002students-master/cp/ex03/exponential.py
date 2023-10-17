"""Exercise 3.9: Exponential function."""


def exponential(x: float, n: int) -> float:
    """Compute the exponential :math:`x^n` using recursion.

    First focus on the case where :math:`n=0`, then :math:`n > 0` and finally :math:`n < 0`.

    :param x: the base number :math:`x`.
    :param n: the power :math:`n`.
    :return: the computed value.
    """
    # TODO: Code has been removed from here.
    if n == 0:
        return 1
    if n < 0:
        k = 1/exponential(x, -n)
        return k
    else:
        e = x*exponential(x, n-1)
        return e


if __name__ == "__main__":
    a = float(input("Enter number x: "))
    y = int(input("Enter number n: "))
    z = exponential(a, y)

    print(f"{a} to the power of {y} = {z}")

