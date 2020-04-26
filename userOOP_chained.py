class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
    def make_deposit (self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(self.name, "- Balance:", self.account_balance)
        return self
    def transfer_money(self, account, amount):
        self.account_balance -= amount
        account.account_balance += amount
        print(self.name, "- Balance:", self.account_balance)
        print(account.name, "- Balance:", account.account_balance)
        return self


guido = User("Guido van Rossum", "guido@python.com")
monty = User("Monty Python", "monty@python.com")
bonzi = User("BonziBuddy", "BonziBuddy@buddy.com")

guido.make_deposit(100).make_deposit(100).make_deposit(200).make_withdrawal(50).display_user_balance()

monty.make_deposit(150).make_deposit(345).make_withdrawal(170).make_withdrawal(65).display_user_balance()

bonzi.make_deposit(500000).make_withdrawal(5).make_withdrawal(3).make_withdrawal(462841).display_user_balance()

guido.transfer_money(bonzi, 100)