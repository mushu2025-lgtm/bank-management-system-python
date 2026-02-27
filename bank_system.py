class BankAccount:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            self.transactions.append(f"Deposited ₹{amount}")
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Invalid withdrawal amount.")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrawn ₹{amount}")
            print(f"₹{amount} withdrawn successfully.")

    def check_balance(self):
        print(f"Current Balance: ₹{self.balance}")

    def display_details(self):
        print("\n--- Account Details ---")
        print(f"Name: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Balance: ₹{self.balance}")

    def show_transactions(self):
        print("\n--- Transaction History ---")
        if not self.transactions:
            print("No transactions yet.")
        else:
            for transaction in self.transactions:
                print(transaction)


def main():
    name = input("Enter account holder name: ")
    account_number = input("Enter account number: ")

    account = BankAccount(name, account_number)

    while True:
        print("\n===== Bank Menu =====")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Display Account Details")
        print("5. View Transactions")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            try:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "2":
            try:
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
            except ValueError:
                print("Please enter a valid number.")

        elif choice == "3":
            account.check_balance()

        elif choice == "4":
            account.display_details()

        elif choice == "5":
            account.show_transactions()

        elif choice == "6":
            print("Thank you for using our banking system.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()