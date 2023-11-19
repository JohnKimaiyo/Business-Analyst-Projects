

import numpy as np
arr = np.array([1, 2, 3])


import pandas as pd
df = pd.read_csv('data.csv')


import seaborn as sns
sns.scatterplot(x='x_column', y='y_column', data=df)

import matplotlib.pyplot as plt
plt.plot(x, y)
plt.show()


from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=3)
kmeans.fit(X)

from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


