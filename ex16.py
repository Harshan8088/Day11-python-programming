# controlled balance update

class bankaccount:
    def __init__(self,balance):
        self.__balance=balance

    def deposit(self,amount):
        if amount>0:
            self.__balance+=amount

    def get_balance(self):
        return self.__balance

account=bankaccount(1000)
account.deposit(500)
print(account.get_balance())