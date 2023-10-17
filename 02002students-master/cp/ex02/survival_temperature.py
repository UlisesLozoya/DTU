"""Exercise 2.6: Calculate the lowest survival temperature."""


def survival_temperature(metabolic_heat: int, thermal_conductance: float):
    """Calculate and print the lowest survival temperature.

    :param metabolic_heat: the metabolic heat production.
    :param thermal_conductance: the thermal conductance.
    """
    # TODO: Code has been removed from here.
    M = metabolic_heat
    g = thermal_conductance
    T = 36 - (0.9 * M - 12) * (g + 0.95) / (27.8 * g)
    T = round(T, 1)

    return print(f'Survival temperature is {T} degrees.')


if __name__ == '__main__':
    x = int(input("Enter metabolic heat: "))
    y = float(input("Enter thermal conductance: "))
    survival_temperature(x, y)
