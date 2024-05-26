class Account:
    def __init__(self, account_number, balance=0):
        self.account_number = account_number
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            return amount
        else:
            print("Insufficient funds")
            return 0

    def get_balance(self):
        return self.balance


class Customer:
    def __init__(self, name):
        self.name = name
        self.accounts = []  # Aggregation: Customer has a list of accounts

    def add_account(self, account):
        self.accounts.append(account)

    def get_total_balance(self):
        return sum(account.get_balance() for account in self.accounts)


class Bank:
    def __init__(self):
        self.customers = []  # Aggregation: Bank has a list of customers

    def add_customer(self, customer):
        self.customers.append(customer)

    def transfer_funds(self, from_account, to_account, amount):
        amount_withdrawn = from_account.withdraw(amount)
        if amount_withdrawn > 0:
            to_account.deposit(amount_withdrawn)
            print("Transfer successful")
        else:
            print("Transfer failed")


# Creating bank, customers, and accounts
bank = Bank()

# Composition: Creating customers with their accounts
customer1 = Customer("Alice")
customer2 = Customer("Bob")

account1 = Account("123456")
account2 = Account("654321")

customer1.add_account(account1)
customer2.add_account(account2)

bank.add_customer(customer1)
bank.add_customer(customer2)

# Sending messages to perform banking operations
account1.deposit(1000)
account2.deposit(500)

print("Alice's total balance:", customer1.get_total_balance())
print("Bob's total balance:", customer2.get_total_balance())

# Polymorphism: Sending message to transfer funds between accounts
bank.transfer_funds(account1, account2, 300)

print("Alice's total balance after transfer:", customer1.get_total_balance())
print("Bob's total balance after transfer:", customer2.get_total_balance())
