from turtle import color
import numpy as np
import matplotlib
matplotlib.use("module://imgcat")
import matplotlib.pyplot as plt
plt.style.use('../mplstyle/iTerm2.mplstyle')


x = np.array([0, 1, 2, 3])
y = np.array([3, 7, 4, 8])

plt.scatter(x, y)
plt.show()