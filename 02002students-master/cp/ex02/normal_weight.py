"""Exercise 2.5: Calculate the normal weight range for a given height."""
import math


def normal_weight(height: float):
    """Calculate and print the range of normal weights for a given height.

    :param height: the height.
    """

    # TODO: Code has been removed from here
    wlow = math.ceil(18.5 * (height ** 2))
    whigh = math.floor(25 * (height ** 2))
    return print(f"Normal weight is between {wlow} and {whigh} kg.")


if __name__ == '__main__':
    x = float(input("What is your height? "))
    normal_weight(x)
