import numpy as np
import matplotlib
matplotlib.use("module://imgcat")
import matplotlib.pyplot as plt
plt.style.use('../mplstyle/iTerm2.mplstyle')


x = np.linspace(-5, 5, 300)
y = x ** 2

plt.plot(x, y)
plt.show()