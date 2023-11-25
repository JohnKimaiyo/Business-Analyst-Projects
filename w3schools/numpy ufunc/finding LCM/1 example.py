# example 1
import numpy as np

num1 = 4
num2 = 6

x = np.lcm(num1, num2)

print(x)

# example 2
import numpy as np

arr = np.array([3, 6, 9])

x = np.lcm.reduce(arr)

print(x)