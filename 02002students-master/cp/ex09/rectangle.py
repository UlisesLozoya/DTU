"""The Rectangle-exercises 9.1-9.3."""
from cp.ex09.vector import Vector

class Rectangle:
    """A class that represents a Rectangle."""

    def __init__(self, width, height, x_c, y_c):
        self.width = width
        self.height = height
        self.x_c = x_c
        self.y_c = y_c

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * (self.width + self.height)

    def get_corners(self):
        x_mid = self.x_c
        y_mid = self.y_c
        half_width = self.width / 2
        half_height = self.height / 2
        coordinate1 = [x_mid - half_width, y_mid - half_height]
        coordinate2 = [x_mid - half_width, y_mid + half_height]
        coordinate3 = [x_mid + half_width, y_mid + half_height]
        coordinate4 = [x_mid + half_width, y_mid - half_height]
        corners = ([coordinate1[0], coordinate2[0], coordinate3[0], coordinate4[0]],
                   [coordinate1[1], coordinate2[1], coordinate3[1], coordinate4[1]])
        return corners

    def translate(self, vector: Vector):
        self.x_c += vector.x
        self.y_c += vector.y


if __name__ == '__main__':
    r = Rectangle(2, 2, 1, 1)
    print(r.get_corners())
    r.translate(Vector(1, 1))
    print(r.get_corners())
