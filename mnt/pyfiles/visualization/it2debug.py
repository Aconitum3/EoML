# Using iTerm2
import numpy as np
import matplotlib
matplotlib.use("module://imgcat")
import matplotlib.pyplot as plt
plt.style.use('../mplstyle/iTerm2.mplstyle')


def f(x,y):
    return x**2 + y**2 / 4

x = np.linspace(-5, 5, 300)
y = np.linspace(-5, 5, 300)
xmesh, ymesh = np.meshgrid(x, y)
z = f(xmesh, ymesh)

colors = [str(i/7) for i in range(1,8)]
levels = range(7)

fig = plt.figure(dpi = 300)
ax = fig.add_subplot(1,1,1)

ax.contourf(x, y, z, colors = colors, levels = levels)
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_title('Title')
plt.show()