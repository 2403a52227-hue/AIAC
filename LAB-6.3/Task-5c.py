class BankAccount:
    def __init__(self, name, starting_balance):
        self.name = name
        self.balance = starting_balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return f"Deposited ${amount:.2f}. New balance: ${self.balance:.2f}"
        else:
            return "Invalid deposit amount. Amount must be positive."
    def withdraw(self, amount):
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                return f"Withdrew ${amount:.2f}. New balance: ${self.balance:.2f}"
            else:
                return "Insufficient funds. Withdrawal denied."
        else:
            return "Invalid withdrawal amount. Amount must be positive."
    def check_balance(self):
        return f"Account holder: {self.name}\nCurrent balance: ${self.balance:.2f}"
# Interactive Bank Account Program
if __name__ == "__main__":
    print("=== Bank Account Management System ===")
    # Get user input for account creation
    name = input("Enter account holder name: ")
    while True:
        try:
            starting_balance = float(input("Enter starting balance: $"))
            if starting_balance >= 0:
                break
            else:
                print("Starting balance cannot be negative. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    # Create the bank account
    account = BankAccount(name, starting_balance)
    print(f"\nAccount created successfully!")
    print(account.check_balance())
    # Main menu loop
    while True:
        print("\n" + "="*40)
        print("Choose an option:")
        print("1. Deposit money")
        print("2. Withdraw money")
        print("3. Check balance")
        print("4. Exit")
        print("="*40)
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            # Deposit
            try:
                amount = float(input("Enter amount to deposit: $"))
                print(account.deposit(amount))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == "2":
            # Withdraw
            try:
                amount = float(input("Enter amount to withdraw: $"))
                print(account.withdraw(amount))
            except ValueError:
                print("Invalid input. Please enter a valid number.")
        elif choice == "3":
            # Check balance
            print(account.check_balance())
        elif choice == "4":
            # Exit
            print("Thank you for using Bank Account Management System!")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")
