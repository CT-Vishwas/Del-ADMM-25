class Shape:
    def __init__(self, name):
        self.name = name

    def perimeter(self, side):
        pass

    def area(self, side):
        pass

class Circle(Shape):
    def __init__(self, name, radius):
        super().__init__(name)
        self.radius = radius
    
    def perimeter(self):
        return 2 * 3.14 * self.radius
    
    def area(self):
        return 3.14 * (self.radius ** 2)

class Square(Shape):
    def __init__(self, name, side):
        super().__init__(name)
        self.side = side
    
    def perimeter(self):
        return 4 * self.side
    
    def area(self):
        return self.side ** 2


if __name__ == '__main__':
    shapes = [Circle('Circle', 2), Square('Square', 4)]
    for shape in shapes:
        print(f"Area of {shape.name} is {shape.area()}")
        print(f"Perimeter of {shape.name} is {shape.perimeter()}")