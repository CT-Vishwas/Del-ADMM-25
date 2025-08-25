class Person:
    __slots__ = ['name', 'age']  # Restricting attributes to save memory
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

if __name__ == '__main__':
    person = Person("Alice", 30)
    person.greet()

    # person.salary = 50000  # Dynamically adding an attribute
    # print(f"{person.name}'s salary is {person.salary}")

    del person.age  # Deleting an attribute

    print(person.__dict__)