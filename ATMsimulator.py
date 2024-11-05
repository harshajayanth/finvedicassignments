class ATMSimulator:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def check_balance(self):
        print(f"Your current balance is: ${self.balance}")

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited: ${amount}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount must be positive.")
        elif amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Successfully withdrew: ${amount}")

    def start(self):
        while True:
            print("\nWelcome to the ATM")
            print("1. Check Balance")
            print("2. Deposit")
            print("3. Withdraw")
            print("4. Exit")

            choice = input("Please choose an option (1-4): ")

            if choice == '1':
                self.check_balance()
            elif choice == '2':
                amount = float(input("Enter amount to deposit: "))
                self.deposit(amount)
            elif choice == '3':
                amount = float(input("Enter amount to withdraw: "))
                self.withdraw(amount)
            elif choice == '4':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid option. Please try again.")

# Example usage
if __name__ == "__main__":
    atm = ATMSimulator(initial_balance=1000)  # Starting balance of $1000
    atm.start()
