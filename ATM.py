import datetime

class User:
    def __init__(self, user_id, pin):
        self.user_id = user_id
        self.pin = pin
        self.account = None

class Account:
    def __init__(self, user, balance=0):
        self.user = user
        self.balance = balance
        self.history = History()

    def deposit(self, amount):
        self.balance += amount
        self.history.add_transaction("Deposit", amount)

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            self.history.add_transaction("Withdrawal", -amount)
        else:
            print("Insufficient balance!")

    def transfer(self, recipient_account, amount):
        if self.balance >= amount:
            self.balance -= amount
            recipient_account.balance += amount
            self.history.add_transaction(f"Transfer to {recipient_account.user.user_id}", -amount)
            recipient_account.history.add_transaction(f"Transfer from {self.user.user_id}", amount)
        else:
            print("Insufficient balance!")

class ATM:
    def __init__(self):
        self.users = []
        self.current_user = None
        self.current_user_account = None

    def authenticate_user(self, user_id, pin):
        for user in self.users:
            if user.user_id == user_id and user.pin == pin:
                self.current_user = user
                self.current_user_account = user.account
                return True
        return False

    def show_menu(self):
        print("ATM INTERFACE")
        print("1. DEPOSIT")
        print("2. WITHDRAW")
        print("3. TRANSFER")
        print("4. HISTORY")
        print("5. QUIT")

    def perform_transaction(self, choice):
        if choice == 1:
            amount = float(input("Enter deposit amount: "))
            self.current_user_account.deposit(amount)
            print(f"Deposited ${amount} successfully.")
        elif choice == 2:
            amount = float(input("Enter withdrawal amount: "))
            self.current_user_account.withdraw(amount)
        elif choice == 3:
            recipient_id = input("Enter recipient's user ID: ")
            recipient_account = self.get_account_by_user_id(recipient_id)
            if recipient_account:
                amount = float(input("Enter transfer amount: "))
                self.current_user_account.transfer(recipient_account, amount)
            else:
                print("Recipient not found.")
        elif choice == 4:
            self.show_transaction_history()
        elif choice == 5:
            self.logout()
        else:
            print("Invalid choice.")

    def get_account_by_user_id(self, user_id):
        for user in self.users:
            if user.user_id == user_id:
                return user.account
        return None

    def show_transaction_history(self):
        print("Transaction History:")
        for transaction in self.current_user_account.history.transactions:
            print(transaction)

    def logout(self):
        self.current_user = None
        self.current_user_account = None

    def run(self):
        while True:
            if not self.current_user:
                user_id = input("Enter user ID: ")
                pin = input("Enter PIN: ")
                if self.authenticate_user(user_id, pin):
                    print(f"Welcome, {user_id}!")
                else:
                    print("Authentication failed. Please try again.")
                    continue

            self.show_menu()
            choice = int(input("Enter your choice: "))
            if choice == 5:
                break
            self.perform_transaction(choice)

class Transaction:
    def __init__(self, description, amount):
        self.description = description
        self.amount = amount
        self.timestamp = datetime.datetime.now()

    def __str__(self):
        return f"{self.timestamp}: {self.description} ${self.amount}"

class History:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, description, amount):
        transaction = Transaction(description, amount)
        self.transactions.append(transaction)

if __name__ == "__main__":
    atm = ATM()
    user1 = User("user123", "1234")
    user2 = User("user456", "5678")
    user3 = User("user789", "9876")
    atm.users.extend([user1, user2, user3])

    user1_account = Account(user1, 1000)
    user2_account = Account(user2, 500)
    user3_account = Account(user3, 1500)

    user1.account = user1_account
    user2.account = user2_account
    user3.account = user3_account

    while True:
        print("Welcome to the ATM")
        user_id = input("Enter your user ID: ")
        pin = input("Enter your PIN: ")
        if atm.authenticate_user(user_id, pin):
            atm.run()
        else:
            print("Authentication failed. Please try again.")
