"""Exercise: Convert length in foot and inch to centimeter."""
import math


def unit_conversion(foot: int, inch: int):
    """Convert length in foot and inch to centimeter.

    :param foot: foot portion of the length in imperical unit.
    :param inch: inch portion of the length in imperical unit.
    """
    ftin = foot * 12
    intotal = ftin + inch
    incm = round(intotal * 2.54)

    return print(f"{foot} ft {inch} in is equal to {incm} cm.")


if __name__ == "__main__":
    x = int(input("Enter feet: "))
    y = int(input("Enter inches: "))
    unit_conversion(x, y)
