import numpy as np
import math as math

class UnivariateLinearRegression:
    def ols_estimate_coefficients(self,x, y):
        c = x.shape[0]
        m_x = np.mean(x)
        m_y = np.mean(x)

        #https://math.stackexchange.com/questions/1499752/sxx-in-linear-regression#:~:text=Sxx%20is%20the,(y%E2%88%92%C2%AFy).
        SS_xy = np.sum(y*x) - (c * m_y * m_x) #Similar Covariance but to be true covariance needs to be divided by n
        SS_xx = np.sum(x*x) - (c * m_x * m_x) #Similar to variance but to be true variance needs to be divided by n
        b_1 = SS_xy / SS_xx
        b_0 = m_y - (b_1 * m_x)
        return b_0, b_1

    def predict(self, x, w, b):
        return np.dot(x, w) + b

    def cost_function(self, y_pred, y_actual):
        m = len(y_pred)
        diff = (np.subtract(y_pred, y_actual))
        diff_squared = np.square(diff)
        diff_squared_sum = np.sum(diff_squared)
        return diff_squared_sum / (2 * m)

    def update_weights(self, alpha, x, y, w, b, m):
        y_pred = self.predict(x, w, b)
        dw = (1 / m) * np.dot(x.T, (y_pred - y))
        db = (1 / m) * np.sum(y_pred - y)
        w = w - alpha * dw
        b = b - alpha * db
        return b, w

    def fit(self, x, y, alpha=0.01, num_iters=1000, threshold=0.0001, initial_w = 0, initial_b = 0, print_statement= False):
        m = x.shape[0]
        w = initial_w  #Initial Estimates
        b = initial_b  #Initial Estimates
        for i in range(num_iters):
            previous_cost = self.cost_function(self.predict(x, w, b), y)
            b, w = self.update_weights(alpha, x, y, w, b, m)
            current_cost = self.cost_function(self.predict(x, w, b), y)
            if ((previous_cost - current_cost) > threshold):
                if print_statement:
                    print("Iteration {0:5d}:  current cost is {1:.5f} and previous cost is {2:.5f} "
                          "and diff is {3:.6f}".format(i+1, current_cost, previous_cost, previous_cost - current_cost))
            else:
                print("Final Iteration {0:5d}:  current cost is {1:.5f} and previous cost is {2:.5f} "
                      "and diff is {3:.6f}".format(i+1, current_cost, previous_cost, previous_cost - current_cost))
                return b, w
        return b, w

    def test(self):
        # observations / data
        x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])

        # estimating coefficients
        b = self.ols_estimate_coefficients(x, y)
        print("Estimated coefficients using OLS: b_0 = {} & b_1 = {}".format(b[0], b[1]))

        b, w = self.fit(x, y, 0.01, 1000, 0.0001)
        print("Estimated coefficients using Gradient Descent: b_0 = {} & b_1 = {}".format(b, w))

if __name__ == "__main__":
    reg = UnivariateLinearRegression()
    reg.test()