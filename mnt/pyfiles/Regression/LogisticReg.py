import numpy as np
from scipy import linalg

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

class LogisticRegression:
    def __init__(self, max_iter = 1000, tol = 1e-6, random_seed = 0):
        self.max_iter = max_iter
        self.tol = tol
        self.beta_ = None
        self.random_state = np.random.RandomState(random_seed)

    def fit(self, X, y):
        X = np.c_[np.ones(X.shape[0]), X]
        self.beta_ = self.random_state.randn(X.shape[1])
        diff = np.inf
        beta_prev = self.beta_
        for _ in range(self.max_iter):
            yhat = sigmoid(np.dot(X, self.beta_))
            r = np.clip(yhat * (1 - yhat), 1e-10, np.inf) # rの要素を任意の範囲内に収める
            XR = X.T * r
            XRX = np.dot(XR, X)
            beta_prev = self.beta_
            b = np.dot(XR, np.dot(X, self.beta_) - 1/r * (yhat - y))
            self.beta_ = linalg.solve(XRX, b)
            if abs(beta_prev - self.beta_).mean() <= self.tol:
                break

    def predict(self, X):
        X = np.c_[np.ones(X.shape[0]), X]
        yhat = sigmoid(np.dot(X, self.beta_))
        return np.where(yhat > .5, 1, 0)

if __name__ == '__main__':
    from sklearn.datasets import load_breast_cancer
    data = load_breast_cancer()
    X = data.data
    y = data.target
    print(X[:400,])
    LogReg = LogisticRegression()
    LogReg.fit(X[:400,],y[:400,])
    print(LogReg.beta_)

    y_pred = LogReg.predict(X[400:,])
    hit = (y[400:,] == y_pred).sum()
    print('Accuracy:', hit/(X.shape[0] - 400))
    
