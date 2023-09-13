from math import pow


class ZeroCouponBonds:
    def __init__(self, principal, maturity, interest_rate):
        self.principal = principal
        self.maturity = maturity
        self.interest_rate = interest_rate

    def compute_present_value(self, x, n):
        return x * pow(1 + self.interest_rate, -n)

    def compute_price(self):
        return self.compute_present_value(self.principal, self.maturity)


if __name__ == '__main__':
    bond = ZeroCouponBonds(1000,2,0.04)
    print("Price of bond in $ = ", bond.compute_price())
