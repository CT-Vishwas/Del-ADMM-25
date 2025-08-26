from random import randint

class BankAccount:
    def __init__(self, balance):
        self.customer_id = self.generate_customer_id()
        self.balance = balance

    def generate_customer_id(self):
        return 'BA'+ str(randint(1,1000))
    
    def get_balance(self):
        return self.balance
    
    def get_customer_id(self):
        return self.customer_id

class SBAccount(BankAccount):
    def __init__(self, balance, customer_name='UNKNOWN'):
        super().__init__(balance)
        self.customer_name = customer_name
        self.customer_id = self.generate_customer_id(10,20)

    def get_customer_name(self):
        return self.customer_name
    
    def generate_customer_id(self, min_val, max_val):
        return 'SBA'+ str(randint(min_val,max_val))
    
if __name__ == '__main__':
    account = SBAccount(customer_name='Vishwas', balance=20000)
    print(f'Customer_id: {account.get_customer_id()}')
    print(f'Account Balance: {account.get_balance()}')
    print(f'Customer Name: {account.get_customer_name()}')


    account1 = BankAccount(1000)
    print(f'Customer_id: {account.get_customer_id()}')
    print(f'Account Balance: {account.get_balance()}')