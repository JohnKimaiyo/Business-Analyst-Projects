#numpy arrays
import numpy as np

a = np.array([1, 2, 3, 4, 5, 6])
print(a[0])

A = np.array([
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'i']
])

print(A[:, :2])


a = np.arange(5)
a + 20