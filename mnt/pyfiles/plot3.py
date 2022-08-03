import numpy as np
import matplotlib.pyplot as plt
import iTerm2

x = np.linspace(-5, 5, 300)
y1 = x ** 2
y2 = (x - 2) ** 2

plt.plot(x, y1)
plt.plot(x, y2, linestyle = "--")
plt.show()