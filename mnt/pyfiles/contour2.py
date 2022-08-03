import numpy as np
import matplotlib.pyplot as plt
import iTerm2

def f(x, y):
    return x ** 2 + y ** 2 / 4

x = np.linspace(-5, 5, 300)
y = np.linspace(-5, 5, 300)
xmesh, ymesh = np.meshgrid(x, y)
z = f(xmesh, ymesh)

plt.contourf(x, y, z, levels = range(1,11))
plt.show()
