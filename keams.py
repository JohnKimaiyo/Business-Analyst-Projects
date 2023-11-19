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