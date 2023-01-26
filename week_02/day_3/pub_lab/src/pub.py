class Pub:
    def __init__(self, name, till):
        self.name = name
        self.till = till
        self.drinks = []

    def increase_till(self, amount):
        self.till += amount
    
    def serve(self, drink, customer):
        if self.drinks.count(drink) == 0 or customer.age < 18 or customer.drunkness > 10:
            return
        if customer.wallet >= drink.price:
            self.drinks.remove(drink)
            customer.buy_drink(drink)
            self.increase_till(drink.price)
            customer.decrease_wallet(drink.price)   
        
