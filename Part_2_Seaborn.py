# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.4.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# ## Part 2 - Visualization with Seaborn and beyond

import pandas as pd
data = pd.read_csv('mtcars.csv')
# %matplotlib inline

data.head()

from sklearn.linear_model import LinearRegression
lm = LinearRegression()
lm.fit(data.iloc[:,2:12], data.iloc[:,1])

lm.coef_

import seaborn as sns
sns.regplot(x="cyl", y = "mpg", data = data)

for i in range(0,5):
    print(i)


