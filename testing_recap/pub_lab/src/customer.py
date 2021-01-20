class Customer:
    def __init__(self, name, wallet):
        self.name = name 
        self.wallet = wallet

    def spend_money(self, money_spent):
        self.wallet -= money_spent

    def buy_drink(self, drink, pub):
        self.spend_money(drink)
        pub.increase_till_money(self.wallet)
        
    