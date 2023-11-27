import pandas as pd

# Creating a DataFrame with NaN values
data = {'Name': ['Alice', 'Bob', 'Charlie', 'David'],
        'Age': [25, 30, None, 22],
        'Salary': [50000, 60000, 75000, None]}

df = pd.DataFrame(data)

# Displaying the original DataFrame
print("Original DataFrame:")
print(df)
# Output:
#      Name   Age   Salary
# 0   Alice  25.0  50000.0
# 1     Bob  30.0  60000.0
# 2  Charlie   NaN  75000.0
# 3   David  22.0      NaN

# Using isna() to check for NaN values
nan_values = df.isna()

# Displaying the result
print("\nDataFrame with True/False indicating NaN values:")
print(nan_values)
# Output:
#     Name    Age  Salary
# 0  False  False   False
# 1  False  False   False
# 2  False   True   False
# 3  False  False    True
