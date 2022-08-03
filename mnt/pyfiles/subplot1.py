import numpy as np
import matplotlib.pyplot as plt
import iTerm2

x = np.linspace(-5, 5, 300)
y = [np.sin(x), np.cos(x)]

fig, axes = plt.subplots(2, 1)

for i in range(2):
    axes[i].set_ylim([-1.5, 1.5])
    axes[i].plot(x, y[i])
plt.show()