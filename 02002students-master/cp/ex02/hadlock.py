"""Exercise: Estimate fetal weight using Hadlock formula."""
import math


def hadlock(head_circ: float, abdominal_circ: float, femur_length: float):
    """Estimate fetal weight using Hadlock formula.

    :param head_circ: head circumference in cm.
    :param abdominal_circ: abdominal circumference in cm.
    :param femur_length: femur length in cm.
    """
    # TODO: Code has been removed from here.
    HC = head_circ
    AC = abdominal_circ
    FL = femur_length
    exp = 1.326 + 0.0107 * HC + 0.0438 * AC + 0.158 * FL - 0.00326 * AC * FL
    EFW = round(10 ** exp, 1)
    return print(f"The estimated fetal weight is {EFW} g.")


if __name__ == "__main__":
    x = float(input("Enter the head circumference in cm: "))
    y = float(input("Enter the abdominal circumference in cm: "))
    z = float(input("Enter the femur length in cm: "))
    hadlock(x, y, z)
