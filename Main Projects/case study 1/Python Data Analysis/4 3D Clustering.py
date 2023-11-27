# Kmean Clustering
# import libraries
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import plotly as py
import plotly.graph_objs as go


from sklearn.cluster import KMeans

import warnings
warnings.filterwarnings("ignore")

# step 1

X3 = df[["Age","Annual Income (k$)","Spending Score"]]
inertia = []
for n in range(1,11):
    algorithm = (KMeans(n_cluster = n,init = "K means++",n_init = 10,max_iter = 300,
                        tol = 0.001, random_state = 111 ,agorithm = 'elkam'))
    algorithm.fit(x3)
    inertia.append(algorithm.inertia_)


# step 2

plt.figure(1,figsize = (15,6))
plt.plot(np.arange(1,11), inertia, "0")
plt.plot(np.arange(1,11),inertia,"-",alpha = 0.5)
plt.ylabel("inertia")
plt.show()


#  step 3
algorith = (KMeans (n_clusters = 6 ,init = "Kmeans++", n_init = 10,max_iter = 300;
            tol = 0.001,random_state = 111, algorithm = "elkan"))
algorithm.fit(X3)
label3 = algorithm.labels_.
centroids3 = algorithm.cluster_centers_


y_kmeans = algorithm.fit_predict(X3)
df["cluster"] = pd.DataFrame(y_kmeans)
df.head()
            

