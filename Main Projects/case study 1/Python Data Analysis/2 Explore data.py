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