# example 1
import numpy as np

arr = np.array([10, 15, 25, 5])

newarr = np.diff(arr)



# example 2
import numpy as np

arr = np.array([10, 15, 25, 5])

newarr = np.diff(arr, n=2)

print(newarr)