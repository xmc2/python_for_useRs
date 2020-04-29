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

# # Python for R users - Learn by doing
#
# ## Chapter 3: scikit-learn
#
#

# As we learned from last chapter, we will need to read in our data (will will be using pandas). 

import pandas as pd
mtcars = pd.read_csv('mtcars.csv')

# Now that we have this data in a usable format we can use it to model a relationship / make predictions, etc.
# The best library for common statistical methods is sci-kit learn.
#
# However, the way we will import this is a bit different. 
# *Because the functions inside* of a package are nested, we can import specific functions and methods like so:

from sklearn.linear_model import LinearRegression
lm = LinearRegression()

# Here, we imported the LinearRegression class from the linear_model submodule of the sklearn package. While seeminly confusing, nicely arranged packages will make this process fairly easy for us to follow. 
# We also used `lm = LinearRegression()` to store the linear regression method as a particular linear regression.

# Now, we can Identify our x and y variables (just like R, these can be utilized in 'matrix' form by which x may be some nxp matrix. Also of note, Python does not support the common 'formula' sytnax for regression and statistical methodologies. 

y = mtcars.loc[:,['mpg']]
x = mtcars.loc[:,['hp']]

lm.fit(x, y)

lm.coef_

lm.intercept_

30.1 - 0.0682 * 300

lm.predict(300)

# Now, let's conduct another linear regression!

lm2 = LinearRegression()

# /alpha

x2 = mtcars.loc[10:,['hp', 'cyl', 'disp', 'drat', 'vs', 'gear']]
y2 = mtcars.loc[10:,['mpg']]

lm2.fit(x2, y2)

predicted_lm2 = lm2.predict(mtcars.loc[:9,['hp', 'cyl', 'disp', 'drat', 'vs', 'gear']])

((predicted_lm2 - mtcars.loc[:9,['mpg']])**2).sum()


