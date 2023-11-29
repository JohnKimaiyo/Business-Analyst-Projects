from numpy import random

x = random.rand()

print(x)

# example 2
from numpy import random

x = random.randint(100, size=(3, 5))

print(x)

# example  3
from numpy import random

x = random.rand(5)

print(x)

# example 4
from numpy import random

x = random.rand(3, 5)

print(x)

# example 5
from numpy import random

x = random.choice([3, 5, 7, 9])

print(x)

# example 6
from numpy import random

x = random.choice([3, 5, 7, 9], size=(3, 5))

print(x)