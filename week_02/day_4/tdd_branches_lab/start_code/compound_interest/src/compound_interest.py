class CompoundInterest:
    def __init__(self, principal, interest, years):
        self.principal = principal
        self.interest = interest
        self.years = years

    
    def calculate(self):
        result =  self.principal * ( 1 + (self.interest / 12)) ** (12 * self.years)
        return round(result, 2)