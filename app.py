# class Point:
#     deafult_color = "red"

#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     @classmethod
#     def zero(cls):
#         return cls(0, 0)

#     def __str__(self):
#         return f" ({self.x} , {self.y})"

#     def __eq__(self, other):
#         return self.x == other.x and self.y == other.y

#     def __gt__(self, other):
#         return self.x > other.x and self.y > other.y

#     def __add__(self, other):
#         return Point(self.x + other.x, self.y + other.y)

#     def draw(self):
#         print(f"Draw ({self.x} , {self.y})")


# Point.deafult_color = "Yellow"
# point = Point(1, 2)
# print(point.deafult_color)
# print(Point.deafult_color)
# point.draw()
# another = Point(3, 4)
# print(another.deafult_color)
# another.draw()

# point = Point(1, 2)
# other = Point(2, 3)
# print(point + other)

# point.draw()

# class Product:
#     def __init__(self, price):
#         self.price = price

#     @property
#     def price(self):
#         return self.__price

#     @price.setter
#     def price(self, value):
#         if value < 0:
#             raise ValueError("Price cannot be negative.")
#         self.__price = value


# product = Product(-10)

# print(product.price)
# class Animal:
#     def __init__(self):
#         print("Animal Constractor")
#         self.age = 1

#     def eat(self):
#         print("eat")


# class Mammal(Animal):
#     def __init__(self):
#         super().__init__()
#         print("Mammal Constractor")
#         self.weight = 2

#     def walk(self):
#         print("walk")


# class Fish(Animal):
#     def swim(self):
#         print("swim")


# m = Mammal()

# print(m.age)
# print(m.weight)


# class InvalidOperationError(Exception):
#     pass


# class Stream(ABC):
#     def __init__(self):
#         self.opened = False

#     def open(self):
#         if self.opened:
#             raise InvalidOperationError("Stream is already open")
#         self.opened = True

#     def close(self):
#         if not self.opened:
#             raise InvalidOperationError("Stream is already close")
#         self.opened = False

#     @abstractmethod
#     def read(self):
#         pass


# class FileStream(Stream):
#     def read(self):
#         print("Read Data from file")


# class NetworkStream(Stream):
#     def read(self):
#         print("Read Data from network")


# class MemoryStream(Stream):
#     def read(self):
#         print("Reading data from a memory stream")


# stream = MemoryStream()
from ecommerce.shopping import sales
sales.calc_tax()
