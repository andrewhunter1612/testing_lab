class Pub:
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
        self.stocklist = []
        self.food_list = []
    
    def increase_till_money(self, increase):
        self.cash += increase

    def add_food(self, food):
        self.food_list.append(food)

    def add_stocklist(self, drink):
        self.stocklist.append(drink)

    def remove_drink_from_stocklist(self, drink):
        for item in self.stocklist:
            if item.name == drink.name:
                self.stocklist.remove(item)

    def check_drink_is_in_stock(self, drink, customer):
        for item in self.stocklist:
            if item.name == drink.name:
                self.sell_drink(drink, customer)

    def check_age(self, customer):
        return customer.age >= 18
    
    def check_drunkenness(self, customer):
        return customer.drunkenness <10
    
    def sell_drink(self, drink, customer):
        if self.check_age(customer) and self.check_drunkenness(customer):
            self.cash += drink.price
            customer.spend_money(drink.price)
            print(customer.wallet)
            self.remove_drink_from_stocklist(drink)
            customer.have_drink(drink)
        else:
            print("You are too young, soz")
            
    def remove_food(self, food):
        for item in self.food_list:
            if item == food.name:
                self.food_list.remove(item)

    def sell_food(self, food, customer):
        self.increase_till_money(food.price)
        customer.spend_money(food.price)
        self.remove_food(food)
        customer.eat_food(food)