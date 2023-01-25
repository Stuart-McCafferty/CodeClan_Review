class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def increase_till(self, amount):
        self.till += amount
    
    def serve(self, drink, customer):
        if self.drinks.count(drink) == 0:
            return
        self.drinks.remove(drink)
        customer.buy_drink(drink)
        self.till += drink.price    
        
