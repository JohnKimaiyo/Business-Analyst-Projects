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





X2 = df[["Age","Spending Score (1-100)"]].iloc[:,:].values
inertia = []
for n in range (1,15):
    algorithm = (KMeans(n_clusters = n ,init = "K-means++",n_init = 10, max_iter =  300,
                       tol = 0.001, random_state = 111, algorithm = "elkan"))
    algorithm.fit(X1)
    inertia.append(algorithm.inertia_)


plt.figure(1,figure =(15,6))
plt.plot(np.arange(1,15),inertia,"0")
plt.plot(np.arange(1,15),inertia,"_",aplpha= 0.5)
plt.xlabel("Numberof clusters "),plt.ylabel("Inertia")
plt.show()





algorithm = (KMeans(n_cluster = 5, init = "k-means++",n_init = 10 , max_iter = 300,
                   tol = 0.0001, random_state = 111, algorith = "elkan"))
algorithm.fit(x2)
label2 = algorithm.labels_
centroids2 = algorithm.cluster_center_

h = 0.02
x_min, x_max = x2[:,0].min() - 1, x2[:0].max() +1
y_min ,y_max = X2[:,1].min() - 1,X2[:,1].max() + 1
xx, yy = np.meshgrid(np.c_[xx.ravel(),yravel()])
z2 = algorithm.predict(np.c_[xx.ravel(),yy.ravel()])
plt.figure(1,figsize = (15,7))
plt.clf()
z2 = z2.reshape(xx.shape)
plt.imshow(z2, interpolation = "nearest",
          extent = (xx.min(), xx.max(),yy.max()),
           cmap = plt.cm.Paste12,aspect = "auto",origin ="lower")
plt.scatter(x = "Annual Income(k$)", y =  "Spending Score (1-100)",data = df , c =labels2 , s = 100)
plt.ylabel("Spending Score (1-100),plt.xlabel"),plt.xlabel("Annual Income(k$)")
plt.show()   



