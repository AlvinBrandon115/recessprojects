from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass
    
    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, l, w):
        self.l, self.w = l, w
    def area(self):
        return self.l * self.w
    def perimeter(self):
        return 2 * (self.l + self.w)

class Circle(Shape):
    def __init__(self, r):
        self.r = r
    def area(self):
        return math.pi * self.r ** 2
    def perimeter(self):
        return 2 * math.pi * self.r

# Test
rect = Rectangle(10, 5)
circle = Circle(7)

print(f"Rectangle - Area: {rect.area():.2f}, Perimeter: {rect.perimeter():.2f}")
print(f"Circle - Area: {circle.area():.2f}, Perimeter: {circle.perimeter():.2f}")