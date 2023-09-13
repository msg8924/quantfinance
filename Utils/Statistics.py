from math import pow
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


if __name__ == '__main__':
    xs = [1, 2, 3, 4, 5, 6]
    ps = [1 / 6] * 6

    mean = compute_expected_value(xs,ps)
    variance = compute_variance(xs,ps)
    std_dev = pow(variance, 0.5)

    print("Mean is %.2f" % mean)
    print("Variance is %.2f" % variance)
    print("Standard Deviation is %.2f" % std_dev)

