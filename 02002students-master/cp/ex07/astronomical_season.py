"""Exercise 7.9: Astronomical season."""


def seasons_numbers(x: int) -> str:
    if 320 <= x <= 620:
        season = "spring"
    elif 621 <= x < 923:
        season = "summer"
    elif 923 <= x < 1221:
        season = "autumn"
    else:
        season = "winter"
    return season


def astronomical_season(date: tuple) -> str:
    """Return the astronomical season of the given date.
    :param date: Tuple with the given date.
    :return: String with astronomical season
    """
    # TODO: Code has been removed from here.
    month_name_to_month_number = {
        "jan": 1,
        "feb": 2,
        "mar": 3,
        "apr": 4,
        "may": 5,
        "jun": 6,
        "jul": 7,
        "aug": 8,
        "sep": 9,
        "oct": 10,
        "nov": 11,
        "dec": 12,
    }
    month = month_name_to_month_number[date[1]]
    good_date = [date[0], month]
    y = int(str(good_date[0]).zfill(2))
    x = int(int(good_date[1]) * 100 + y)
    seasons = seasons_numbers(x)
    return seasons


if __name__ == "__main__":
    print(astronomical_season((23, "sep")))
