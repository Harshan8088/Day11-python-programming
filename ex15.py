# private attribute

class bankaccount:
    def __init__(self,balance):
        self.balance=balance

    def show_balance(self):
        print("balance",self.__balance)

account=bankaccount(5000)
account.show_balance()