class Customer:
    def __init__(self, name, wallet, age):
        self.name = name 
        self.wallet = wallet
        self.age = age
        self.drunkenness = 0

    def spend_money(self, money_spent):
        self.wallet -= money_spent

    def have_drink(self, drink):
        self.drunkenness += drink.alcohol_level

    def eat_food(self, food):
        if self.drunkenness > 0:
            self.drunkenness -= food.decrease_drunkenness()        
    