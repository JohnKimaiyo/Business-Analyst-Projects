

# Import the Pandas library
import pandas as pd

# Create a data frame in Python
# Using the same student dataset

# Creating a data frame
students_data = pd.DataFrame({
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [22, 23, 21, 22],
    'Score': [85, 90, 78, 95]
})

# Print the data frame
print(students_data)

# Accessing specific columns
names = students_data['Name']
ages = students_data['Age']
scores = students_data['Score']

# Accessing specific rows
first_student = students_data.loc[0, :]

# Filtering data based on conditions
high_scores = students_data[students_data['Score'] > 90]
