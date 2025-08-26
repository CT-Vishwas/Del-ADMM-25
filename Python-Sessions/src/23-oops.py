from abc import ABC, abstractmethod

class Shape(ABC): # Inherit from ABC to make it an abstract base class
    @abstractmethod
    def area(self):
        """Calculates the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Calculates the perimeter of the shape."""
        pass

    def description(self):
        """A concrete method that can be inherited as is."""
        return "This is a geometric shape."

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14159 * self.radius

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# This would raise a TypeError because Shape is abstract
# s = Shape()

circle = Circle(5)
rectangle = Rectangle(4, 6)

shapes = [circle, rectangle]

for shape in shapes:
    print(f"Shape: {shape.__class__.__name__}")
    print(f"Area: {shape.area():.2f}")
    print(f"Perimeter: {shape.perimeter():.2f}")
    print(f"Description: {shape.description()}\n")