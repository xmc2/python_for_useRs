# -*- coding: utf-8 -*-
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
# ## Part 1: Pandas & Basic Syntax
# ### Basics and importing Pandas
#   
#
# Welcome! This will be my attempt to share a little of what I know about python for those (like myself) whom primarily use R for data wrangling, reporting, and analysis. Python is a general purpose language being used in many from web development, to deep learning. Since it is versitile, the language doesn't come 'data analysis ready' right out of the box as much as R does. For example, there is not concept of a data frame in 'base' python as there is in base R. In order to gain these capibilities we will need to import the pandas library (library is analogous to a package in R).
#
# We will do that with an import statement as so:

import pandas

# `import pandas` is nearly the same as calling `library(pandas)`
#   
# Or, more commonly we can use the following:

import pandas as pd

# The second part of the above statement `as pd` nicknames pandas as pd to save us some typing :)
#
# The pandas library contains a function `read_csv` which reads csv files into a data frame, just like R. Similarly to R, we can call functions specifically from a library. Like `reader::read_csv`, we can use `pandas.read_csv`, or in this example because we imported pandas `as pd`, we can use: `pd.read_csv`.  We will access by typing `pd.read_csv('csvfile.csv')` which is analagous to, in R, `reader::read_csv('csvfile.csv')`. An important difference is these functions are not simply dumped into the global namespace like in R where `library(readr)` would make available all of readr's functions globably. This can cause some issues, but luckily R usually informs you of this (if you've ever tried to use dplyr you've seen such a warning about the select function). 

mtcars = pd.read_csv('mtcars.csv')

# While the first argument of the read_csv function is the path to the data, there are more too (however, are not required). To get help for a function, type: '?function'. In this case we would type: `?pd.read_csv` to hear all about the function its arguemnets, etc. This is nearly identical to typying `package::functionname?` in R.

# ?pd.read_csv

# Great! Now we have our data, now what? Well, lets explore. First, we can look at the first few rows by using the head method.

mtcars.head()

# And the tail method.

mtcars.tail()

# or what if we want some summary statistics?

mtcars.describe()

# Awesome!
#
# You may have noticed that in R, we would have used functions like `head(mtcars)`, `tail(mtcars)`, or `summary(mtcars)`. In python, it is common to see the function call following the 'object' and a dot. This is utilziing an object's method. In these cases, our object is our pandas data frame, and out method is the function (head, tail, describe, etc.). We can think of a method as a function that “belongs to” an object. We couldn't just 

# An important part of any work with data frames is being able to look at certain columns or rows.
#   
# Luckily, pandas' data frames have some methods for us to use!
#
# Firstly, we can pass a list to our data frame to select the columns by name likeso:

mtcars[['mpg', 'hp']].head()

# There are also special methods which help us select data, `.loc` for label based indexing or
# `.iloc` for positional indexing

mtcars.loc[:5,['model',"cyl",'hp']]

mtcars.iloc[[0,1],[0,1]]

mtcars.iloc[[0,1],[0,1]]

mtcars["mpg"].mean()

mtcars.mean()

# Say we want to scale miles per gallon to Km per Liter, we could do that by multiplying MPG by ~.425144

mtcars["kpg"] = mtcars["mpg"] * 0.425144 # to km/l

mtcars[['mpg','kpg']]

mtcars[mtcars['mpg'] > 25]

# We know one of the most powerful functions in R is the `apply` statment and its sister functions. Pandas has defined a similar method for dataframes conveniently called apply. the first argument we invoke is the function, followed by the index (the data argument is by default the dataframe the apply statement is stemming from, we can think of it almost like a pipe).
# Type `?pd.DataFrame.apply` for more!

mtcars[['mpg', 'hp']].apply(sum,1)

# ?pd.DataFrame.apply


