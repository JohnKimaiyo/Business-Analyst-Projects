#What is NumPy? NumPy is a Python library used for working with arrays. It also has functions for working in domain of linear algebra, fourier transform, and matrices.
import numpy as np
#Whereas Pandas is used for creating heterogenous, two-dimensional data objects
import pandas as pd
#Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations
import matplotlib.pyplot as plt
#Seaborn is a library for making statistical graphics in Python
import seaborn as sns
#Plotly is an open-source module of Python that is used for data visualization and supports various graphs like line charts, scatter plots, bar charts, histograms, area plots, et
import plotly as py

import plotly.graph_objs as go
#What is K-means used for?
#K-means clustering, a part of the unsupervised learning family in AI, is used to group similar data points together in a process known as clustering. 
from sklearn.cluster import KMeans


import warnings
warnings.filterwarnings("ignore")
df = pd.read_csv(r"C:\Users\jki\Desktop\Python Customer Sgementation Project Zero\project 2\customers.csv")
df.head()

df.columns

df.info()

df.describe()

#When creating plots using Matplotlib, you get a default figure size of 6.4 for the width and 4.8 for the height (in inches).
df.isnull().sum()

plt.figure(1, figsize = (15,6))
n = 0
for x in ["Age","Annual_Income (k$)","Spending_Score (1-100)"]:
    n += 1
    plt.subplot(1,3,n)
    plt.subplots_adjust(hspace = 0.5,wspace = 0.5)
    sns.distplot(df[x],bins = 15)
    plt.title("Distplot of {}".format(x))
    plt.show()

    sns.pairplot(df,vars = ["Spending Score(1-100)","Annual Income(k$)","Age"],hue="Gender")