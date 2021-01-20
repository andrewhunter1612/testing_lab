class Food:
    def __init__(self, name, price, rejuvanation_level):
        self.name = name
        self.price = price
        self.rejuvanation_level = rejuvanation_level

    def decrease_drunkenness(self):
        return self.rejuvanation_level
