from math import pow
import numpy as np
from random import sample

import SimulatingRandomVariables

def compute_expected_value(xs, ps = None):
    mean = 0.0
    if ps != None:
        for index, tuple in enumerate(zip(xs,ps)):
            number = tuple[0] * tuple[1]
            mean += tuple[0] * tuple[1]
        return mean
    return np.mean(xs)


def compute_variance(xs, ps):
    # E[X-U] = E[X^2] - E[X]^2
    mean = compute_expected_value(xs,ps)
    mean_squared = mean**2
    xs_squared = [pow(x,2) for x in xs]
    mean_x_squared = compute_expected_value(xs_squared, ps)
    return mean_x_squared - mean_squared

def compute_covariance(xs,xps, ys,yps):
    mean_x = compute_expected_value(xs,xps)
    mean_y = compute_expected_value(ys,yps)
    n = len(xs)

    sum = 0
    for index, tuple in enumerate(zip(xs,ys)):
        xi = tuple[0]
        yi = tuple[1]
        sum += (xi-mean_x) * (yi-mean_y)

    return sum / n

def compute_correlation(xs,xps,ys,yps):
    std_dev_x = compute_variance(xs,xps)
    std_dev_y = compute_variance(ys,yps)
    covariance = compute_covariance(xs,xps, ys,yps)

    return covariance / (std_dev_y * std_dev_x)


if __name__ == '__main__':
    xs = [1, 2, 3, 4, 5, 6]
    ps = [1 / 6] * 6

    ys = [1, 2, 3, 4, 5, 6]
    yps =[1 / 6] * 6

    mean = compute_expected_value(xs,ps)
    variance = compute_variance(xs,ps)
    std_dev = pow(variance, 0.5)
    covariance = compute_covariance(xs,ps,ys,yps)
    correlation = compute_correlation(xs, ps, ys,yps)


    print("Mean is %.2f" % mean)
    print("Variance is %.2f" % variance)
    print("Standard Deviation is %.2f" % std_dev)
    print("Covariance is %.2f" % covariance)
    print("Correlation is %.2f" % correlation)


    print("Generate Correlated MultiVariates")

    random = SimulatingRandomVariables.generate_multivariate_normal(0,1,0,1,0.5,1000)
    r1 = random[:,0]
    r2 = random[:,1]
    print(r1)
    print(r2)

    mean = compute_expected_value(r1,None)
    variance = compute_variance(r1,None)
    std_dev = pow(variance, 0.5)
    covariance = compute_covariance(r1,None,r2,None)
    correlation = compute_correlation(r1, None, r2,None)


    print("Mean is %.2f" % mean)
    print("Variance is %.2f" % variance)
    print("Standard Deviation is %.2f" % std_dev)
    print("Covariance is %.2f" % covariance)
    print("Correlation is %.2f" % correlation)


