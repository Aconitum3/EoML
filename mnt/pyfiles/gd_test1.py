import numpy as np
import matplotlib.pyplot as plt
import gd
import iTerm2

def f(xx):
    x = xx[0]
    y = xx[1]
    return 5 * x**2 - 6 * x * y + 3 * y**2 + 6 * x - 6 * y

def df(xx):
    x = xx[0]
    y = xx[1]
    return np.array([10 * x - 6 * y + 6, -6 * x + 6 * y - 6])

algo = gd.GradientDescent(f, df)
initial = np.array([1, 1])
algo.solve(initial)
print('x =', algo.x_)
print('optim :', algo.opt_)

plt.scatter(initial[0], initial[1])
plt.plot(algo.path_[:, 0], algo.path_[:, 1])

xs = np.linspace(-2, 2, 300)
ys = np.linspace(-2, 2, 300)

xmesh, ymesh = np.meshgrid(xs, ys)
xx = np.r_[xmesh.reshape(1, -1), ymesh.reshape(1, -1)]
levels = [-3, -2.9, -2.8, -2.6, -2.4, -2.2, -2, -1, 0, 1, 2, 3, 4]

plt.contour(xs, ys, f(xx).reshape(xmesh.shape), levels = levels, linestyles = "dotted")
plt.show()