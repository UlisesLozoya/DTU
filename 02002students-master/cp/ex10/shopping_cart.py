"""This file contains the project's code and solution."""


class Item:
    """A class to represent an inventory item."""

    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    def __lt__(self, item2) -> bool:
        value_1 = self.quantity * self.price
        value_2 = item2.quantity * item2.price
        if value_1 < value_2:
            return True
        else:
            return False

    def __gt__(self, item2) -> bool:
        value_1 = self.quantity * self.price
        value_2 = item2.quantity * item2.price
        if value_1 > value_2:
            return True
        else:
            return False

    def __eq__(self, item2) -> bool:
        value_1 = self.quantity * self.price
        value_2 = item2.quantity * item2.price
        if value_1 == value_2:
            return True
        else:
            return False


class Inventory:
    """A class to represent an inventory of items."""

    def __init__(self):
        self.listitems = []

    def add_item(self, item: Item):
        item_as_list = [item.name, float(item.quantity), float(item.price)]
        self.listitems.append(item_as_list)
        return self.listitems

    def calculate_total_value(self):
        value = 0
        for i in self.listitems:
            q = i[1]
            p = i[2]
            value = value + q * p

        return int(value)

    def __lt__(self, other) -> bool:
        value1 = self.calculate_total_value()
        value2 = other.calculate_total_value()
        if value1 < value2:
            return True
        else:
            return False

    def __gt__(self, other) -> bool:
        value1 = self.calculate_total_value()
        value2 = other.calculate_total_value()
        if value1 > value2:
            return True
        else:
            return False

    def __eq__(self, other) -> bool:
        value1 = self.calculate_total_value()
        value2 = other.calculate_total_value()
        if value1 == value2:
            return True
        else:
            return False
