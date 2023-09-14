from numpy.random import multivariate_normal

def generate_multivariate_normal(mean_x,var_x, mean_y, var_y, cov, n):
    cov_matrix = [[var_x, cov],
                  [cov,var_y]]
    return multivariate_normal([mean_x, mean_y], cov_matrix, n)


if __name__ == '__main__':
    print(generate_multivariate_normal(0,1,0,1,0.5,100))