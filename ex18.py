# shopping cart

class shoppingcart:
    def __init__(self):
        self.items=[]

    def add_item(self,name,price):
        self.items.append((name,price))

    def total(self):
        return sum(price for name, price in self.items)


cart=shoppingcart()
cart.add_item("mouse",400)
cart.add_item("keyboard",1000)

print("total bill:",cart.total())