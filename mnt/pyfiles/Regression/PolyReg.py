import LinearReg
import numpy as np

class PolynomialRegression:
    def __init__(self, degree):
        self.degree = degree
    
    def fit(self, x, y):
        x_pow = []
        xx = x.reshape(len(x), 1)
        for i in range(1, self.degree + 1):
            x_pow.append(xx ** i)
        mat = np.concatenate(x_pow, axis = 1)

        linreg = LinearReg.LinearRegression()
        linreg.fit(mat, y)
        self.beta_ = linreg.beta_

    def predict(self, x):
        r = 0
        for i in range(self.degree + 1):
            r += self.beta_[i] * x**i
        return r

if __name__ == '__main__':

    # Poly
    # ------------------------------------------------------------------------------------------------------------------
    np.random.seed(0)

    def f(x):
        return 1 + 2 * x

    x = np.random.random(10) * 10
    y = f(x) + np.random.randn(10)
    x1 = x.min() - 1
    x2 = x.max() + 1

    Poly = PolynomialRegression(6)
    Poly.fit(x, y)
    xx = np.linspace(x.min(), x.max(), 300)
    yy = np.array([Poly.predict(u) for u in xx])

    print('beta:', Poly.beta_)
    print('predict (1, 1):', Poly.predict(np.array([1, 1])))

    LR = LinearReg.LinearRegression()
    LR.fit(x,y)
    b, a = LR.beta_

    # plot
    # ------------------------------------------------------------------------------------------------------------------
    import matplotlib
    matplotlib.use("module://imgcat")
    import matplotlib.pyplot as plt
    plt.style.use('../../mplstyle/iTerm2.mplstyle')

    fig = plt.figure(figsize = (12,12), dpi = 200)
    ax = fig.add_subplot(1, 1, 1)
    ax.scatter(x, y)
    ax.plot([x1, x2], [a*x1+b, a*x2+b], 
            color = '#F675A8', 
            linestyle = 'dashed')  # 線形回帰
    ax.plot(xx, yy)                # 多項式回帰


    plt.show()
