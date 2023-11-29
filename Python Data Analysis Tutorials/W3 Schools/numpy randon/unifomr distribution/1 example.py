# example 1
from numpy import random

x = random.uniform(size=(2, 3))

print(x)

# example 2
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.uniform(size=1000), hist=False)

plt.show()