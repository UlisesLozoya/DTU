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


if __name__ == "__main__":
    inventory = Inventory()
    item1 = Item("Laptop", 10, 800)
    item2 = Item("Phone", 20, 400)
    item3 = Item("Tablet", 15, 300)
    item4 = Item("Laptop", 2, 850)
    item5 = Item("Phone", 5, 420)

    inventory.add_item(item1)
    inventory.add_item(item2)
    inventory.add_item(item3)

    inventory2 = Inventory()
    inventory2.add_item(item2)
    inventory2.add_item(item4)
    inventory2.add_item(item5)

    inventory3 = Inventory()
    inventory3.add_item(item3)
    inventory3.add_item(item4)
    inventory3.add_item(item5)

    print(inventory.listitems)
    print(inventory2.listitems)
    print(inventory3.listitems)
    inventory.calculate_total_value()
    inventory2.calculate_total_value()
    inventory3.calculate_total_value()
