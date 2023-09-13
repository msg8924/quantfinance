from math import exp
from math import pow

def computeYield(pv, cpn):
    return cpn/pv


def computePVBond(x, r, n,t, cpn):
    pv = 0
    for i in range(0,n*t):
        pv += computePV(cpn/n,r/n,1,i+1)
    pv += computePV(x,r,n,t)
    return pv

def computePV(x, r,n, t):
    return x * pow(1+ r/n, -t*n)

def computeFV(x, r,n, t):
    return x * pow(1+r/n,t*n)

def computeCPV(x,r,t):
    return x * exp(-r*t)
def computeCFV(x,r,t):
    return x * exp(r * t)

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
   print(computeCPV(1000,r,t))

   print(cpv)
   print(cfv)

   bondPV = computePVBond(1000,0.04,1,3,100)
   print(computeYield(bondPV,100)*100)
