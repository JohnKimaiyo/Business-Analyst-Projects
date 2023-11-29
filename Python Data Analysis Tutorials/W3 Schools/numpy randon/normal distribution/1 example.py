# example 1
from numpy import random

x = random.normal(size=(2, 3))

print(x)

# example 2
from numpy import random

x = random.normal(loc=1, scale=2, size=(2, 3))

print(x)

# example 3
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(size=1000), hist=False)

plt.show()