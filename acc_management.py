class Bank:
    total_balance = 0 

    @classmethod
    def deposit(cls, deposited_money):
        cls.total_balance += deposited_money
        print("Money deposited:", deposited_money)
        cls.get_balance()

    @classmethod
    def withdrawal(cls, requested_amount):
        if requested_amount > cls.total_balance:
            print("Insufficient funds")
        else:
            cls.total_balance -= requested_amount
            print("Money withdrawn:", requested_amount)
            cls.get_balance()

    @classmethod
    def get_balance(cls):
        print("Total Balance:", cls.total_balance)

# Example usage
Bank.deposit(1000) 
Bank.withdrawal(500)
Bank.withdrawal(600)  
