# Demonstration of metaclasses in Python

# Define a simple metaclass
class MyMeta(type):
    def __new__(cls, name, bases, dct):
        print(f"Creating class {name} with MyMeta")
        dct['meta_added'] = True
        return super().__new__(cls, name, bases, dct)

# Use the metaclass in a class definition
class MyClass(metaclass=MyMeta):
    def __init__(self, value):
        self.value = value

    def show(self):
        print(f"Value: {self.value}")

# Instantiate and use the class
obj = MyClass(42)
obj.show()
print(f"meta_added attribute: {obj.meta_added}")