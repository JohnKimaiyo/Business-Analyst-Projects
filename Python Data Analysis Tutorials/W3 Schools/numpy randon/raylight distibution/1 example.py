# example 1
from numpy import random

x = random.rayleigh(scale=2, size=(2, 3))

print(x)

# example 2
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.rayleigh(size=1000), hist=False)

plt.show()

# example 3
