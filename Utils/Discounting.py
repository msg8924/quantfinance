from math import exp
from math import pow

def compute_yield(pv, cpn):
    return cpn/pv

def compute_pv_coupon_bond(x, r, n, t, cpn):
    pv = 0
    for i in range(0,n*t):
        pv += compute_pv(cpn / n, r / n, 1, i + 1)
    pv += compute_pv(x, r, n, t)
    return pv

def compute_pv(x, r, n, t):
    return x * pow(1+ r/n, -t*n)

def compute_fv(x, r, n, t):
    return x * pow(1+r/n,t*n)

def compute_cpv(x, r, t):
    return x * exp(-r*t)
def compute_cfv(x, r, t):
    return x * exp(r * t)


'''
if __name__ == '__main__':
   x = 100
   r = 0.04
   t = 1
   n = 1

   fv = computeFV(x,r,n,t)
   pv = computePV(fv, r,n, t)

   print(pv)
   print(fv)


   cfv = computeCFV(x, r,t)
   cpv = computeCPV(cfv,r,t)

   print(computePV(1000,r,n,t))
   print(computePVCouponBond(1000,0.04,1,3,100))

   print(cpv)
   print(cfv)

   bondPV = computePVCouponBond(1000,0.04,1,3,100)
   print(computeYield(bondPV,100)*100)
'''