class Pub:
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
    
    def increase_till_money(self, increase):
        self.cash += increase
    
    def sell_drink(self, drink, customer):
        if customer.age >= 18 and customer.drunkenness < 10:
            self.cash += drink.price
            customer.wallet -= drink.price
            customer.drunkenness += drink.alcohol_level
        else:
            print("You are too young, soz")
   
            