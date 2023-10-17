"""Exercise 5.11. Best Buy."""


def best_buy(prices: list, money: int, start_index: int, reverse: bool) -> int:
    """Return the number of items that can be bought with the given amount of money. The function should be able to handle arbitrary starting points and to run the list in reverse.

    :param prices: list of prices
    :param money: amount of money
    :param start_index: starting index in list
    :param reverse: boolean to indicate if list should be run in reverse
    :return: number of items that can be bought with the given amount of money
    """
    # TODO: Code has been removed from here.
    prices.sort()
    if reverse:
        prices.sort(reverse=True)
    bought = 0
    i = 0
    total_price = 0
    while i < len(prices):
        total_price = total_price + prices[i]
        bought = bought + 1
        i = i + 1
        if total_price == money:
            break
        elif total_price > money:
            bought = bought - 1
            break
    return bought


if __name__ == "__main__":
    prices = [3, 2, 1, 3, 5]
    print(best_buy([3, 2, 1, 3, 5], 15, 4, True))
    print(best_buy(prices, 20, 4, False))
