# example 1
import numpy as np

arr = np.arange(1, 10)

print(np.log2(arr))

# example 2
import numpy as np

arr = np.arange(1, 10)

print(np.log10(arr))

# example 3
from math import log
import numpy as np

nplog = np.frompyfunc(log, 2, 1)

print(nplog(100, 15))

# exapmle 4
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.add(arr1, arr2)

print(newarr)

# examplpe 3
import numpy as np

arr1 = np.array([1, 2, 3])
arr2 = np.array([1, 2, 3])

newarr = np.sum([arr1, arr2])

print(newarr)