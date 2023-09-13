from math import pow
from random import sample
def compute_expected_value(xs, ps):
    mean = 0.0;
    for index, tuple in enumerate(zip(xs,ps)):
        number = tuple[0] * tuple[1]
        mean += tuple[0] * tuple[1]

    return mean


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



if __name__ == '__main__':
    xs = [1, 2, 3, 4, 5, 6]
    ps = [1 / 6] * 6

    ys = sample(range(0,1000),6)
    yps =[1 / 6] * 6

    mean = compute_expected_value(xs,ps)
    variance = compute_variance(xs,ps)
    std_dev = pow(variance, 0.5)
    covariance = compute_covariance(xs,ps,ys,yps)

    print("Mean is %.2f" % mean)
    print("Variance is %.2f" % variance)
    print("Standard Deviation is %.2f" % std_dev)
    print("Covariance is %.2f" % covariance)
