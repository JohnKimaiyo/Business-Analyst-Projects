# import libraries
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt 
from sklearn.cluster import KMeans 
sns.set()
from sklearn  import preprocessing


import data
url = "https://archive.ics.uci.edu/ml/machine-learning-databases/00352/Online%20Retail.xlsx"
data = pd.read_excel(url)

# describe the data
data.describe()

#plot data
plt.scatter(data["Quantity"],data["UnitPrice"])
plt.xlabel('Quantity')
plt.ylabel("UnitPrice")

# Scale data
x_scaled = preprocessing.scale(x)
x_scaled

#Find the number of centroids
for i in range(1,10):
kmeans = KMeans(i)
kmeans.fit(x_scaled)
wcss.append(kmeans.inertia_)


plt.plot(range(1,10),wcss)
plt.xlabel('Number of Clusters')
plt.ylabel('WCSS')

# Predict clusters
Kmeans_news = Kmeans(4)
Kmeans_new.fit(x_scaled)
cluster_new["cluster_pred"] = kmeans_new_predict(x_scaled)