"""Exercise 3.4: Body Temperature."""


def body_temperature(temperature: float):
    """Calculate the body's response based on the given temperature.
    
    :param temperature: The temperature in degrees Celsius.
    :return: The body's response as a string.
    """
    # TODO: Code has been removed from here.
    if temperature < 35:
        return "Hypothermia"
    if 35 <= temperature <= 37:
        return "Normal"
    if 37 < temperature <= 38:
        return "Slight fever"
    if 38 < temperature <= 39:
        return "Fever"
    if temperature > 39:
        return "Hyperthermia"


if __name__ == "__main__":
    x = float(input("Enter your body temperature: "))
    print(body_temperature(x))

