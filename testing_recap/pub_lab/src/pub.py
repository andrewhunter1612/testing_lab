class Pub:
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        self.stocklist = ["Beer"]
    
    def increase_till_money(self, increase):
        self.cash += increase

    def remove_drink_from_stocklist(self, drink):
        for item in self.stocklist:
            if item == drink.name:
                self.stocklist.remove(item)

    def check_drink_is_in_stock(self, drink, customer):
        for item in self.stocklist:
            if item == drink.name:
                self.sell_drink(drink, customer)

    def check_age(self, customer):
        return customer.age >= 18
    
    def check_drunkenness(self, customer):
        return customer.drunkenness <10
    
    def sell_drink(self, drink, customer):
        if self.check_age(customer) and self.check_drunkenness(customer):
            self.cash += drink.price
            customer.wallet -= drink.price
            self.remove_drink_from_stocklist(drink)
        else:
            print("You are too young, soz")
        customer.have_drink(drink)
            