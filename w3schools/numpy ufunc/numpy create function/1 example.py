# example 1
import numpy as np

def myadd(x, y):
  return x+y

myadd = np.frompyfunc(myadd, 2, 1)

print(myadd([1, 2, 3, 4], [5, 6, 7, 8]))


# example 2
import numpy as np

print(type(np.add))

# example 3
import numpy as np

print(type(np.concatenate))