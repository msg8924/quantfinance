from Utils import Discounting
from Bonds import Bonds

class CouponBonds(Bonds):

    def __init__(self, principal, maturity, interest_rate, coupon):
        super().__init__(principal, maturity, interest_rate)
        self.coupon = coupon

    def compute_present_value(self, x, n):
        return Discounting.compute_pv_coupon_bond(x, self.interest_rate, 1, self.maturity, self.coupon)

    def compute_price(self):
        return self.compute_present_value(self.principal, self.maturity)

if __name__ == '__main__':
    bond = CouponBonds(1000,3,0.04,100)
    bond.print_price()