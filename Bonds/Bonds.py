class Bonds:
    def __init__(self, principal, maturity, interest_rate):
        print('Bonds Constructor Called')
        self.principal = principal
        self.maturity = maturity
        self.interest_rate = interest_rate

    def compute_present_value(self, x, n):
        pass

    def compute_price(self):
        pass

    def print_price(self):
        print("Price of bond in $ = ", self.compute_price())