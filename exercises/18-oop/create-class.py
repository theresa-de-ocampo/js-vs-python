class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self.__balance = balance

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Invalid deposit amount")

        self.__balance += amount

        return self.__balance

    @property
    def balance(self):
        return self.__balance


myAccount = Account("Teriz", 30000)
print(myAccount.owner)
myAccount.deposit(20000)
print(myAccount.balance)
