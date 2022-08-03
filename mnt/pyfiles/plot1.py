# Using iTerm2

import numpy as np
import matplotlib
matplotlib.use("module://imgcat")
import matplotlib.pyplot as plt

x = np.array([0,1,2,3])
y = np.array([3,7,4,8])

fig = plt.figure()
fig.patch.set_alpha(0)

color = '#ffffff'

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

ax.plot(x, y, color = 'r')
plt.show()