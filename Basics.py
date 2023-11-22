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

import pandas as pd

certificates_earned = pd.Series(
    [8, 2, 5, 6],
    index=['Tom', 'Kris', 'Ahmad', 'Beau']
)

print(certificates_earned)