class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Invalid deposit amount")

        self._balance += amount

        return self._balance

    @property
    def balance(self):
        return self._balance


myAccount = Account("Teriz", 30000)
print(myAccount.owner)
myAccount.deposit(20000)
print(myAccount.balance)
