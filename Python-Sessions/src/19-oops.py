class AccessDemo:
    def __init__(self):
        self.public_var = "I am public"
        self._protected_var = "I am protected"
        self.__private_var = "I am private"

    def show_vars(self):
        print("Public:", self.public_var)
        print("Protected:", self._protected_var)
        print("Private:", self.__private_var)

demo = AccessDemo()
demo.show_vars()

# Accessing variables
print(demo.public_var)         # Public: accessible
print(demo._protected_var)     # Protected: accessible, but should be treated as protected
# print(demo.__private_var)    # Private: will raise AttributeError

# Accessing private variable using name mangling
print(demo._AccessDemo__private_var)