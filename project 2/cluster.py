import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

import plotly as py
import plotly.graph_objs as go

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
