from unitgrade import UTestCase, Report
import cp


class Week10TestSnakeCase(UTestCase):
    def test_snake(self):
        from cp.ex10.extended_string import ExtendedString
        self.assertEqual(ExtendedString("WoW This is amazing").to_snake_case(), "wow_this_is_amazing")
        self.assertEqual(ExtendedString("WHAT A SENTENCE").to_snake_case(), "what_a_sentence")
        self.assertEqual(ExtendedString("THIS IS the BEST text ever").to_snake_case(), "this_is_the_best_text_ever")
        self.assertEqual(ExtendedString("123 woW").to_snake_case(), "123_wow")
        self.assertEqual(ExtendedString("wOof").to_snake_case(), "woof")

class Week10TestWordCount(UTestCase):
    def test_word_count(self):
        from cp.ex10.extended_string import ExtendedString
        self.assertTrue(issubclass(ExtendedString, str))
        self.assertEqual(ExtendedString("WoW This is amazing").word_count(), 4)
        self.assertEqual(ExtendedString("WHAT A SENTENCE").word_count(), 3)
        self.assertEqual(ExtendedString("THIS IS the BEST text ever").word_count(), 6)
        self.assertEqual(ExtendedString("123 woW").word_count(), 2)
        self.assertEqual(ExtendedString("wOof").word_count(), 1)

class Week10TestStudent(UTestCase):
    def test_remaining_days(self):
        from cp.ex10.student import Student, Person
        self.assertTrue(issubclass(Student, Person))
        self.assertEqual(Student("Jane", "Smith", "BSc").remaining_ECTS(50), 130)
        self.assertEqual(Student("Alice", "Johnson", "MSc").remaining_ECTS(80), 40)
class Week10TestVectorAdd(UTestCase):
    def test_vector_add(self):
        from cp.ex10.vector import Vector
        v = Vector(1, 2) + Vector(6, 5)
        self.assertEqual(v.x, 7)
        self.assertEqual(v.y, 7)

        v = Vector(3, 5) + Vector(60, 15)
        self.assertEqual(v.x, 63)
        self.assertEqual(v.y, 20)

        v = Vector(10, 21) + Vector(16, 51)
        self.assertEqual(v.x, 26)
        self.assertEqual(v.y, 72)

        v = Vector(11, 12.5) + Vector(26, 15.5)
        self.assertEqual(v.x, 37)
        self.assertEqual(v.y, 28)

        v = Vector(11, 22) + Vector(66, 55)
        self.assertEqual(v.x, 77)
        self.assertEqual(v.y, 77)

class Week10TestVectorSub(UTestCase):
    def test_vector_sub(self):
        from cp.ex10.vector import Vector
        v = Vector(1, 2) - Vector(6, 5)
        self.assertEqual(v.x, -5)
        self.assertEqual(v.y, -3)

        v = Vector(3, 5) - Vector(60, 15)
        self.assertEqual(v.x, -57)
        self.assertEqual(v.y, -10)

        v = Vector(10, 21) - Vector(16, 51)
        self.assertEqual(v.x, -6)
        self.assertEqual(v.y, -30)

        v = Vector(11, 12.5) - Vector(26, 15.5)
        self.assertEqual(v.x, -15)
        self.assertEqual(v.y, -3)

        v = Vector(11, 22) - Vector(66, 55)
        self.assertEqual(v.x, -55)
        self.assertEqual(v.y, -33)

class Week10TestVectorDot(UTestCase):
    def test_vector_dot(self):
        from cp.ex10.vector import Vector
        self.assertEqual(Vector(1, 2) * Vector(6, 5), 16)
        self.assertEqual(Vector(3, 5) * Vector(60, 15), 255)
        self.assertEqual(Vector(10, 20) * Vector(6, 1), 80)
        self.assertEqual(Vector(1, 12) * Vector(26, 5), 86)
        self.assertEqual(Vector(11, -66) * Vector(66, 11), 0)

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
        from cp.ex10.shopping_cart import Item,Inventory

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
        from cp.ex10.shopping_cart import Item,Inventory

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
        from cp.ex10.shopping_cart import Item,Inventory

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
        from cp.ex10.shopping_cart import Item,Inventory

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
            (Week10TestSnakeCase, 10),
            (Week10TestWordCount, 20),
            (Week10TestStudent,20),
            (Week10TestVectorAdd,10),
            (Week10TestVectorSub,20),
            (Week10TestVectorDot,10),
            (Week10TestItemCreate,20),
            (Week10TestItemLessThan,10),
            (Week10TestItemGreaterThan,20),
            (Week10TestItemEquals,10),
            (Week10TestInventoryTotalValue,20),
            (Week10TestInventoryLessThan,10),
            (Week10TestInventoryGreaterThan,20),
            (Week10TestInventoryEquals,10),
            ]


class Week10Tests(Report): 
    title = "Tests for week 10"
    #version = 1.0
    #url = "https://gitlab.compute.dtu.dk/cp/02002students/-/blob/master/cp/tests"
    pack_imports = [cp]
    individual_imports = []
    questions = questions

if __name__ == '__main__':
    from unitgrade import evaluate_report_student
    evaluate_report_student(Week10Tests())
