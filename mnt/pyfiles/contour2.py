# Using iTerm2

import numpy as np
import matplotlib
matplotlib.use("module://imgcat")
import matplotlib.pyplot as plt

color = '#ffffff'

fig = plt.figure()
fig.patch.set_alpha(0)

ax = plt.subplot(1,1,1)

ax.patch.set_alpha(0)

# x and y lables
ax.xaxis.label.set_color(color)
ax.yaxis.label.set_color(color)


# axis color
ax.spines['top'].set_color(color)
ax.spines['bottom'].set_color(color)
ax.spines['left'].set_color(color)
ax.spines['right'].set_color(color)
ax.tick_params(axis = 'x', colors =color)
ax.tick_params(axis = 'y', colors = color)

# contents
def f(x,y):
    return x**2 + y**2 / 4

x = np.linspace(-5, 5, 300)
y = np.linspace(-5, 5, 300)
xmesh, ymesh = np.meshgrid(x, y)
z = f(xmesh, ymesh)

colors = ["0.1", "0.3", "0.5", "0.7"]
levels = [1, 2, 3, 4, 5]

ax.contourf(x, y, z, colors = colors, levels = levels)
plt.show()