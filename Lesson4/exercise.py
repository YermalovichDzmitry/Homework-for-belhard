import math
from abc import abstractmethod, ABC


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class Line:
    def __init__(self, x1, y1, x2, y2):
        self.point_1 = Point(x1, y1)
        self.point_2 = Point(x2, y2)

    def length(self) -> float:
        return round(math.sqrt((self.point_1.x - self.point_2.x) ** 2 + (self.point_1.y - self.point_2.y) ** 2), 3)


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass


class Square(Line, Shape):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)
        self.side = super().length()

    @property
    def area(self) -> float:
        return self.side ** 2

    @property
    def perimeter(self) -> float:
        return self.side * 4


class Rect(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def area(self) -> float:
        return self.a * self.b

    @property
    def perimeter(self) -> float:
        return 2 * (self.a + self.b)


class Cube(Square):
    def __init__(self, x1, y1, x2, y2):
        super().__init__(x1, y1, x2, y2)

    @property
    def volume(self) -> float:
        return self.side ** 3


cube = Cube(1, 0, 1, 4)
print(f"Cube volume = {cube.volume}")
print(f"Сube edge = {cube.side}")
print(f"Сube face area = {cube.area}")
print(f"Сube face perimeter = {cube.perimeter}")

rect = Rect(4, 5)
print("=" * 100)
print(f"Perimeter of the rectangle = {rect.perimeter}")
print(f"Area of the rectangle = {rect.area}")
