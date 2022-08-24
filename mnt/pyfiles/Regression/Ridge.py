import numpy as np
from scipy import linalg

class Ridge:
    def __init__(self, lambda_ = 1.):
        self.beta_ = None       # 回帰係数
        self.intercept = None   # 切片の有無
        self.lambda_ = lambda_  # 正則化パラメータ
    
    def fit(self, X, y, intercept = True):
        self.intercept = intercept
        if self.intercept:
            X = np.c_[np.ones(X.shape[0]), X]
        
        # 方程式 A * beta = b を解く
        A = np.dot(X.T, X) + self.lambda_ * np.eye(X.shape[1])
        b = np.dot(X.T, y)
        self.beta_ = linalg.solve(A, b)
    
    def predict(self, X):
        if X.ndim == 1:
            X = X.reshape(1, -1)
        if self.intercept:
            X = np.c_[np.ones(X.shape[0]), X]
        return np.dot(X, self.beta_)

if __name__ == '__main__':
    n = 100
    scale = 10

    # learning
    # ------------------------------------------------------------------------------------------------------------------
    np.random.seed(0)
    X = np.random.random((n, 2)) * scale
    w0, w1, w2 = 1, 2, 3
    y = w0 + w1 * X[:, 0] + w2 * X[:, 1] + np.random.randn(n)

    model = Ridge(1000.)
    model.fit(X, y)
    print('beta:', model.beta_)
    print('predict (1, 1):', model.predict(np.array([1, 1])))

    # mesh
    # ------------------------------------------------------------------------------------------------------------------
    xmesh, ymesh = np.meshgrid(np.linspace(0, scale, 20),
                               np.linspace(0, scale, 20))
    zmesh = (model.beta_[0] + model.beta_[1] * xmesh.ravel() + model.beta_[2] * ymesh.ravel()).reshape(xmesh.shape)

    # plot
    # ------------------------------------------------------------------------------------------------------------------
    import matplotlib
    matplotlib.use("module://imgcat")
    import matplotlib.pyplot as plt
    plt.style.use('../../mplstyle/iTerm2.mplstyle')

    fig = plt.figure(figsize = (12,12), dpi = 200)
    ax = fig.add_subplot(1,1,1, projection = '3d')
    ax.scatter(X[:,0], X[:,1], y, color = '#44e697')
    ax.plot_wireframe(xmesh, ymesh, zmesh, color = '#F675A8')

    plt.show()