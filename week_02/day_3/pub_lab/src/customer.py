class Customer:
    def __init__(self, name, wallet, age):
        self.name = name
        self.wallet = wallet
        self.age  = age
        self.drunkness = 0
    
    def decrease_wallet(self, amount):
        self.wallet -= amount