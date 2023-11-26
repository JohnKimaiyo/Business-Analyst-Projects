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

# Data Exporation
df = pd.read_csv(r"C:\Users\jki\Desktop\Python Customer Sgementation Project Zero\Main Projects\case study 1\source files\Mall_Customers.csv")
df.head()

# calling our columns
df.columns

# get info
df.info



df.describe()

df.isnull().sum()


plt.figure(1, figsize = (15,6))
n = 0
for x in ["Age", "Annual Income (k$)"]:
    n += 1
    plt.subplot(1,3,n)
    plt.subplots_adjust(hspace = 0.5,wspace = 0.5)
    sns.distplot(df[x], bins = 15)
    plt.title("Distplot of  {}". format (x))
plt.show()


sns.pairplot(df,vars = ["Age", "Annual Income (k$)","Spending Score (1-100)"])

