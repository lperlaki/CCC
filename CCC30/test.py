import numpy as np
import matplotlib.pyplot as plt
from munch import Munch

# Create a 10*10 array with random values from 0-255
a = np.random.randint(0, 255, (10, 10))

# set all avalues in array 0/0 - 5/5 to 0
a[0:5, 0:5] = 0

# Show all non zero values on plot
plt.scatter(*a.nonzero())

plt.show()
