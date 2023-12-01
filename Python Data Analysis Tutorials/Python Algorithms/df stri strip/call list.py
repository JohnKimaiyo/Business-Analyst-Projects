import pandas as pd

# Create a sample DataFrame
data = {"Last_Name": ["123John_", "_Doe", "Smith.456", "Johnson/"]}
df = pd.DataFrame(data)

# Before stripping
print("Before:\n", df)

# Apply the strip operation
df["Last_Name"] = df["Last_Name"].str.strip("123._/")

# After stripping
print("\nAfter:\n", df)
