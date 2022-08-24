import numpy as np
import scipy

def soft_thresholding(x, lambda_):
    return np.sign(x) * max(abs(x) - lambda_, 0)

class Lasso:
    def __init__(self, lambda_ = 1., tol = 1e-6, max_iter = 1000):
        self.lambda_ = lambda_
        self.tol = tol
        self.max_iter = max_iter
        self.beta_ = None

    def fit(self, X, y):
        n, p = X.shape
        self.beta_ = np.zeros(p + 1)  # 初期値
        avgl1 = 0.
        for _ in range(self.max_iter):
            avgl1_prev = avgl1
            self._update(n, p, X, y)
            avgl1 = np.abs(self.beta_).sum() / self.beta_.shape[0]
            if abs(avgl1 - avgl1_prev) <= self.tol:
                break

    def _update(self, n, p, X, y):
        self.beta_[0] = (y - np.dot(X, self.beta_[1:])).sum() / n   # 切片の更新
        b0 = np.ones(n) * self.beta_[0]                             # 切片のベクトル化
        for k in range(p):
            bb = self.beta_[1:]
            bb[k] = 0
            q = np.dot(y - b0 - np.dot(X, bb), X[:, k])
            r = np.dot(X[:, k].T, X[:, k])
            self.beta_[k + 1] = soft_thresholding(q/r, self.lambda_)

if __name__ == '__main__':

    from sklearn.datasets import load_boston
    from sklearn import preprocessing
    boston = load_boston()
    X = boston.data
    y = boston.target
    
    # standardize
    # -----------------------------------------------------------------------------   
    X = preprocessing.scale(X)
    y = y - np.mean(y)

    # path
    # -----------------------------------------------------------------------------
    path = []
    lambda_ = np.linspace(0, 10, 300)
    for i in lambda_:
        lasso = Lasso(lambda_ = i)
        lasso.fit(X, y)
        path.append(lasso.beta_[1:])

    # plot
    # -----------------------------------------------------------------------------
    import matplotlib
    matplotlib.use("module://imgcat")
    import matplotlib.pyplot as plt
    plt.style.use('../../mplstyle/iTerm2.mplstyle')

    fig = plt.figure(figsize = (12,12), dpi = 300)
    ax = fig.add_subplot(1,1,1)
    ax.plot(lambda_, path)
    ax.set_xscale('log')

    plt.show()
