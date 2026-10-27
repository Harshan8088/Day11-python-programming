# common method interface

class upi:
    def pay(self):
        print("paytment using upi")

class card:
    def pay(self):
        print("paytmet using card")

methods=[upi(),card()]

for method in methods:
    method.pay()