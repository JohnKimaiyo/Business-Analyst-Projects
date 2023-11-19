import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Assuming you have a CSV file with customer data, load it into a DataFrame
# Replace 'your_data.csv' with your actual file name and update column names accordingly
df = pd.read_csv('your_data.csv')
# Display the first few rows of the DataFrame to understand the structure of your data
print(df.head())

# Assuming your data has columns like 'Age', 'Income', 'Spending_Score', etc.
# Select relevant columns for segmentation
X = df[['Age', 'Income', 'Spending_Score']]

# Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Determine the optimal number of clusters using the Elbow Method
wcss = []  # Within-Cluster Sum of Squares
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
    kmeans.fit(X_scaled)
    wcss.append(kmeans.inertia_)

# Plot the Elbow Method graph
plt.plot(range(1, 11), wcss)
plt.title('Elbow Method')
plt.xlabel('Number of clusters')
plt.ylabel('WCSS')  # Within-Cluster Sum of Squares
plt.show()

# Based on the Elbow Method, choose the optimal number of clusters
# For simplicity, let's say it's 3 in this example
optimal_clusters = 3

# Perform k-means clustering with the optimal number of clusters
kmeans = KMeans(n_clusters=optimal_clusters, init='k-means++', random_state=42)
df['Cluster'] = kmeans.fit_predict(X_scaled)

# Visualize the clusters in 3D space
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

ax.scatter(df['Age'], df['Income'], df['Spending_Score'], c=df['Cluster'], cmap='viridis')
ax.set_xlabel('Age')
ax.set_ylabel('Income')
ax.set_zlabel('Spending Score')

plt.title('Customer Segmentation')
plt.show()
