from Utils import Discounting
from Bonds import Bonds
class ZeroCouponBonds(Bonds):
    def __init__(self, principal, maturity, interest_rate):
        super().__init__(principal, maturity, interest_rate)

    def compute_present_value(self, x, n):
        return Discounting.compute_pv(x, self.interest_rate, 1, n)

    def compute_price(self):
        return self.compute_present_value(self.principal, self.maturity)


if __name__ == '__main__':
    bond = ZeroCouponBonds(1000,2,0.04)
    bond.print_price()

