import numpy as np

class UnivariateLinearRegression:
    def __init__(self,iterations, learning_rate):
        self.iterations = iterations
        self.learning_rate = learning_rate


    def estimate_coefficients(self,x, y):
        c = x.shape[0]
        m_x = np.mean(x)
        m_y = np.mean(x)

        SS_xy = np.sum(y*x) - (c * m_y * m_x)
        SS_xx = np.sum(x*x) - (c * m_x * m_x)
        b_1 = SS_xy / SS_xx
        b_0 = m_y - (b_1 * m_x)
        return b_0, b_1


    def fit(self, X, Y):
        self.r = X.shape[0]
        self.W = np.zeros(self.r)
        self.b = 0
        self.X = X
        self.Y = Y

        for i in range(self.iterations):
            self.update_weights()

        return self

    def update_weights(self):
        Y_pred = self.predict(self.X)
        dW = - (2 * (self.X.T).dot(self.Y - Y_pred)) / self.r
        db = - 2 * np.sum(self.Y - Y_pred) / self.r
        #W is the bet and b is the intercept
        self.W = self.W - (self.learning_rate * dW)
        self.b = self.b - (self.learning_rate * db)
        return self

    def predict(self, X):
        return X.dot(self.W) + self.b


    def test(self):
        # observations / data
        x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
        y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])

        # estimating coefficients
        b = self.estimate_coefficients(x, y)
        print("Estimated coefficients: b_0 = {} & b_1 = {}".format(b[0], b[1]))



if __name__ == "__main__":
    reg = UnivariateLinearRegression(iterations = 10, learning_rate = 0.01)
    reg.test()