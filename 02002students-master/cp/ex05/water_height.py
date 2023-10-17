"""Exercise 5.10. Water height."""


def water_height(h0: int, r: list) -> int:
    """Calculate the water height after multiple days of rain.

    :param: h0: initial height of the water
    :param: r: list of rain showers
    :return: height of water after days of rain
    """
    # TODO: Code has been removed from here.
    ht1 = h0 + r[0] - 2
    if ht1 < 0:
        ht1 = 0
    ht = 0
    i = 1
    while i <= len(r) - 1:
        ht = ht1 + r[i] - 2
        ht1 = ht
        i = i + 1
    if ht < 0:
        return 0
    return ht


if __name__ == "__main__":
    print(water_height(0, [4, 2, 3]))
