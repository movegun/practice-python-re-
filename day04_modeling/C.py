import numpy as np

import matplotlib.pyplot as plt

x = np.random.uniform(0.0,5.0,100)

print(x)

plt.hist(x)
plt.show()