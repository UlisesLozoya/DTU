"""Exercise 3.6: BAC Calculator."""
import math


def bac_calculator(alcohol_consumed: float, weight: float, gender: str, time: float) -> float:
    """Calculate the blood alcohol concentration based on the alcohol consumed, body weight, and time since consumption.
    
    :param alcohol_consumed: The total amount of alcohol consumed in grams (float)
    :param weight: The person's body weight in kilograms (float)
    :param gender: The person's gender, which must be a string of either "male" or "female" (str)
    :param time: The time elapsed since alcohol consumption in hours (float)
    :return: The calculated blood alcohol concentration (BAC) as a float value.
    """
    # TODO: Code has been removed from here.
    ac = alcohol_consumed
    r = 0
    b = 0
    if gender == "male":
        r = 0.68
        b = 0.015
    elif gender == "female":
        r = 0.55
        b = 0.017
    h = time
    bac = (ac / (r * weight)) * 100 - b * h
    return bac


if __name__ == "__main__":
    x = float(input("Enter alcohol consumed in kilograms: "))
    y = float(input("Enter wight in kilograms: "))
    z = str(input("Enter sex of the person ('male' or 'female'): "))
    t = float(input("Enter the time passed in hours: "))
    print(bac_calculator(x, y, z, t))
