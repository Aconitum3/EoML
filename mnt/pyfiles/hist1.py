import numpy as np
import matplotlib.pyplot as plt
import iTerm2

np.random.seed(0)
l = [np.random.randint(1, 7, size = 10).sum() for _ in range(1000)]

plt.hist(l, bins = 20)
plt.show()