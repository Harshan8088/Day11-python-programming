# bank management system

class bankaccount:
    def __init__(self,name,balance=0):
        self.name=name
        self.__balance=balance

    def deposit(self,amount):
        if amount <=0:
            print("invalid amount")
            return
        self.__balance+=amount
        print("deposit successful")

    def withdraw(self,amount):
        if amount<=0:
            print("invalid amount")
        elif amount>self.__balance:
            print("insufficient balance")
        else:
            self.__balance -=amount
            print("withdrawal successful")

    def balance(self):
        print("balance:Rs.",self.__balance)

name=input("account holder:")
account=bankaccount(name)

while True:
    print("\n---BANKMANAGEMENT---") 
    print("1.Deposit")
    print("2.Withdraw") 
    print("3.CheckBalance")
    print("4.Exit")

    

    choice=input("choice:")

    if choice=="4":
        break

    if choice in ("1","2"):
        try:
            amount=float(input("amount:"))
        except ValueError:
            print("enter a valid number")
            continue

        if choice=="1":
            account.deposit(amount)
        else:
            account.withdraw(amount)

    elif choice =="3":
        account.balance()
    else:
        print("invalid choice")