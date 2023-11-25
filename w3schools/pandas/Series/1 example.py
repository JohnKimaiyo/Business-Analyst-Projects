#  example 1
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a)

print(myvar)

# example 2
import pandas as pd

a = [1, 7, 2]

myvar = pd.Series(a, index = ["x", "y", "z"])

print(myvar)

# example 3
import pandas as pd

calories = {"day1": 420, "day2": 380, "day3": 390}

myvar = pd.Series(calories)

print(myvar)