"""Exercise 3.7: Solar panel."""


def solar_panel(move: bool, swap: bool, hot: bool, empty: bool):
    """Print out whether it is a good idea to install solar panels on an object with the given properties.

    :param move: does the object move around?
    :param swap: does the object allow swapping or recharging battery?
    :param hot: is the object hot to the touch when it is running?
    :param empty: are there other empty places near the object?
    """
    # TODO: Code has been removed from here.
    t = move
    y = swap
    u = hot
    i = empty
    if t and not y and not u:
        return print("maybe")
    elif t and not y and u:
        return print("haha\ngood luck")
    elif t and y:
        return print("probably not")
    elif not t and not i:
        return print("sure")
    elif not t and i:
        return print("probably not")
    elif not t and not y:
        return print("probably not")


if __name__ == "__main__":
    print("Answer with Y or N")
    m = input("Does the object move around?: ")
    if m == 'Y':
        m = True
    elif m == 'N':
        m = False
    s = input("Does the object swap or recharge batteries?: ")
    if s == 'Y':
        s = True
    elif s == 'N':
        s = False
    h = input("Is the object hot when running?: ")
    if h == 'Y':
        h = True
    elif h == 'N':
        h = False
    e = input("Are there empty places around?: ")
    if e == 'Y':
        e = True
    elif e == 'N':
        e = False
    print(solar_panel(m, s, h, e))
