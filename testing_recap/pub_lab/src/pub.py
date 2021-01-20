class Pub:
    def __init__(self, name, cash):
        self.name = name
        self.cash = cash
    
    def increase_till_money(self, increase):
        self.cash += increase
    