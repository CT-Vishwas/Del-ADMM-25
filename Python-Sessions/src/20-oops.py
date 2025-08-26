class MathUtils:
    @classmethod
    def add(self, a, b):
        return a + b
    
    @classmethod
    def sub(self, a, b):
        return a - b
    
    @classmethod
    def mul(self, a, b):
        return a * b
    
    @classmethod
    def div(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero")
        return a / b

    @staticmethod
    def is_even(n):
        return n % 2 == 0
    
if __name__ == '__main__':
    m = MathUtils()
    print(m.add(2, 3))
    print(m.sub(5, 2))
    print(m.mul(3, 4))
    print(m.div(10, 2))

    print(m.is_even(4))
    print(MathUtils.is_even(5))