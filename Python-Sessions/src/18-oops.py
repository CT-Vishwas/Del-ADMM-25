from random import randint

class BankAccount:
    def __init__(self, balance):
        self.customer_id = self.generate_customer_id()
        self._balance = balance

    def generate_customer_id(self):
        return 'BA'+ str(randint(1,1000))
    
    @property
    def balance(self):
        return self._balance
    
    def get_customer_id(self):
        return self.customer_id
    
    @balance.setter
    def balance(self, balance):
        if balance < 0:
            raise ValueError('Balance cannot be negative')
        self._balance = balance


    
if __name__ == '__main__':
    account = BankAccount(20000)
    print(f'Customer_id: {account.get_customer_id()}')
    print(f'Account Balance: {account.balance}')

    account.balance = 50000
    print(f'Account Balance: {account.balance}')