import pandas as pd

# Creating two sample DataFrames
df1 = pd.DataFrame({'key': ['A', 'B', 'C'], 'value': [1, 2, 3]})
df2 = pd.DataFrame({'key': ['A', 'B', 'D'], 'value': [4, 5, 6]})

# Merge the DataFrames on the 'key' column
merged_df = pd.merge(df1, df2, on='key', how='inner')

# Display the result
print(merged_df)
