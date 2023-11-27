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



X3 = df[["Age","Annual Income (k$)","Spending Score"]]
inertia = []
for n in range(1,11):
    algorithm = (KMeans(n_cluster = n,init = "K means++",n_init = 10,max_iter = 300,
                        tol = 0.001, random_state = 111 ,agorithm = 'elkam'))
    algorithm.fit(x3)
    inertia.append(algorithm.inertia_)

    

