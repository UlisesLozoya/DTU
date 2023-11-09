from unitgrade import UTestCase, Report, hide
import math


class Week09VectorDotProduct(UTestCase):
    def test_dot_product_with_positive_vectors(self):
        from cp.ex09.vector import Vector
        vector1 = Vector(2, 3)
        vector2 = Vector(4, 5)
        result = vector1.dot(vector2)
        self.assertEqual(result, vector1.x * vector2.x + vector1.y * vector2.y)

    def test_dot_product_with_negative_vectors(self):
        from cp.ex09.vector import Vector
        vector1 = Vector(-2, -3)
        vector2 = Vector(-4, -5)
        result = vector1.dot(vector2)
        self.assertEqual(result, vector1.x * vector2.x + vector1.y * vector2.y)

    def test_dot_product_with_mixed_vectors(self):
        from cp.ex09.vector import Vector
        vector1 = Vector(2, -3)
        vector2 = Vector(-4, 5)
        result = vector1.dot(vector2)
        self.assertEqual(result, vector1.x * vector2.x + vector1.y * vector2.y)


class Week09TranslatingRectangle(UTestCase):
    def test_move_vector(self):
        from cp.ex09.vector import Vector
        from cp.ex09.rectangle import Rectangle
        r = Rectangle(10, 4, 2, 2)
        r.translate(Vector(2, 3))
        self.assertEqual(r.x_c, 4)
        self.assertEqual(r.y_c, 5)

        r = Rectangle(1, 2, 1, 1)
        r.translate(Vector(4, 2))
        self.assertEqual(r.x_c, 5)
        self.assertEqual(r.y_c, 3)

        r = Rectangle(12, 14, 0, 0)
        r.translate(Vector(-5, 5))
        self.assertEqual(r.x_c, -5)
        self.assertEqual(r.y_c, 5)

        r = Rectangle(12, 13, -5, 2)
        r.translate(Vector(10, 12))
        self.assertEqual(r.x_c, 5)
        self.assertEqual(r.y_c, 14)


class Week10TestItemCreate(UTestCase):
    def test_item_creation(self):
        from cp.ex10.shopping_cart import Item
        item1 = Item("Widget", 10, 5)
        item2 = Item("Gadget", 5, 10)
        item3 = Item("Phone", 11, 14)
        self.assertEqual(item1.name, "Widget")
        self.assertEqual(item2.name, "Gadget")
        self.assertEqual(item3.name, "Phone")
        self.assertEqual(item1.quantity, 10)
        self.assertEqual(item2.quantity, 5)
        self.assertEqual(item3.quantity, 11)
        self.assertEqual(item1.price, 5.0)
        self.assertEqual(item2.price, 10.0)
        self.assertEqual(item3.price, 14.0)


class Week10TestItemLessThan(UTestCase):
    def test_item_less_than_operator(self):
        from cp.ex10.shopping_cart import Item
        item1 = Item("Widget", 10, 5.0)
        item2 = Item("Gadget", 5, 10.0)
        item3 = Item("Phone", 11, 14.0)
        self.assertFalse(item1 < item2)
        self.assertTrue(item1 < item3)
        self.assertTrue(item2 < item3)


class Week10TestItemGreaterThan(UTestCase):
    def test_item_greater_than_operator(self):
        from cp.ex10.shopping_cart import Item
        item1 = Item("Widget", 10, 5.0)
        item2 = Item("Gadget", 5, 10.0)
        item3 = Item("Phone", 11, 14.0)
        self.assertFalse(item1 > item2)
        self.assertFalse(item1 > item3)
        self.assertFalse(item2 > item3)


class Week10TestItemEquals(UTestCase):
    def test_item_equal_operator(self):
        from cp.ex10.shopping_cart import Item
        item1 = Item("Widget", 10, 5)
        item2 = Item("Gadget", 5, 10)
        item3 = Item("Phone", 11, 14)
        self.assertFalse(item2 == item3)
        self.assertFalse(item1 == item3)


class Week10TestInventoryTotalValue(UTestCase):
    def test_inventory_calculate_total_value(self):
        from cp.ex10.shopping_cart import Item, Inventory

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

        inventory.calculate_total_value()
        inventory2.calculate_total_value()
        inventory3.calculate_total_value()

        self.assertEqual(inventory.calculate_total_value(), 20500)
        self.assertEqual(inventory2.calculate_total_value(), 11800)
        self.assertEqual(inventory3.calculate_total_value(), 8300)


class Week10TestInventoryLessThan(UTestCase):
    def test_inventory_less_than_operator(self):
        from cp.ex10.shopping_cart import Item, Inventory

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
        self.assertFalse(inventory < inventory2)
        self.assertFalse(inventory2 < inventory3)
        self.assertFalse(inventory < inventory2)


class Week10TestInventoryGreaterThan(UTestCase):
    def test_inventory_greater_than_operator(self):
        from cp.ex10.shopping_cart import Item, Inventory

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
        self.assertTrue(inventory > inventory2)
        self.assertTrue(inventory2 > inventory3)
        self.assertTrue(inventory > inventory3)


class Week10TestInventoryEquals(UTestCase):
    def test_inventory_equal_operator(self):
        from cp.ex10.shopping_cart import Item, Inventory

        inventory = Inventory()
        item1 = Item("Laptop", 10, 800)
        item2 = Item("Phone", 800, 10.)
        item3 = Item("Tablet", 20, 20.)

        inventory.add_item(item1)

        inventory2 = Inventory()
        inventory2.add_item(item2)

        inventory3 = Inventory()
        inventory3.add_item(item3)
        self.assertTrue(inventory == inventory2)
        self.assertFalse(inventory2 == inventory3)
        self.assertFalse(inventory == inventory3)


questions = [
    (Week09VectorDotProduct, 20),
    (Week09TranslatingRectangle, 20),
    (Week10TestItemCreate, 5),
    (Week10TestItemLessThan, 5),
    (Week10TestItemGreaterThan, 5),
    (Week10TestItemEquals, 5),
    (Week10TestInventoryTotalValue, 5),
    (Week10TestInventoryGreaterThan, 5),
    (Week10TestInventoryLessThan, 5),
    (Week10TestInventoryEquals, 5),
]


class Project5(Report):
    title = "Project 5"
    remote_url = "https://cp.pages.compute.dtu.dk/02002public/_static/evaluation/"

    abbreviate_questions = True
    questions = questions
    import cp
    pack_imports = [cp]


if __name__ == "__main__":
    from unitgrade import evaluate_report_student

    evaluate_report_student(Project5())
