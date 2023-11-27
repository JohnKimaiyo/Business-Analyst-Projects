import pandas as pd

# Creating a sample DataFrame
data = {
    'Category': ['A', 'B', 'A', 'B', 'A', 'B'],
    'Value': [10, 20, 15, 25, 12, 18]
}

df = pd.DataFrame(data)

# Grouping by 'Category'
grouped = df.groupby('Category')

# Calculating the mean value for each group
mean_values = grouped.mean()

print(mean_values)



result = grouped.agg({'Value': ['mean', 'sum']})
print(result)
