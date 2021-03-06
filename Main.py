import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

data = pd.read_csv(r"E:\Python aniket\archive\StatewiseTestingDetails.csv")
data.head()
data.columns
data.describe()
data.isnull().sum()
g=sns.relplot(x="Positive",y="State",data=data,s=10)
g.fig.set_figwidth(10.27)
g.fig.set_figheight(15.7)

g=sns.relplot(x="Positive",y="State",kind="line",data=data)
g.fig.set_figwidth(18.27)
g.fig.set_figheight(22.7)

sns.catplot(x="Positive", y="State", data=data, height=5, aspect=2)

sns.pairplot(data)
