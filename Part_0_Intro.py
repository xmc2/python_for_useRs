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

# # Part 0: Introduction
#
# I've always thought it would be interesting to try to teach R via packages. 
# The first chapter could be on the [readr package](https://readr.tidyverse.org/) - strictly relating to importing and exporting data. Chapter 2 could be [dplyr](https://dplyr.tidyverse.org/), learning how to manipulate, wrangle, and view data. Following this we could explore the 'stats' (or caret perhaps) package for statistical learning, ggplot for visualization, maybe even shiny for dynamic visualizations or web applications. It would be exciting to write - and hard to stop, as the endless packages of the R ecosystem could keep one writing for a long long time. 
# I've also thought it would be important to write a book on [Python](https://www.python.org/) for R users. Many of my friends from graduate school and beyond are intamitaly familiar with R, but havn't picked up Python yet. Many resources out there either teach statistics/data science in Python for those whom already know Python (i.e. are familiar with not only the syntax, and pythonic principals, but also oop) or start from scratch assuming no programming knowlege. Even worse, some place an inordinate amount of attention on some packages like numpy or matplotlib, whcih, while powerful, aren't needed to get a grasp on basic or even intermediate data science work in python. 
#
# ## Structure of this book
#
# This book takes the approach of moving from the ground up, starting with importing data to fancier predictive analytics. Each chapter's focus will be on a python library, emphasising learning the differences between Python and R, the libraries available to Python users, and how to continute to learn python.
#
#

# ## Getting started
#
# Download [anaconda](https://www.anaconda.com/download/). 
#
# ## Beginning similarities and differences
#
# We should first note some similarities and differences between the two languages.
#
# Firstly, the main arithmatic functions are the same between R and Python: +, -, /, and \* are all the same. There are some differences however. \*\* in python is power (2\*\*4) is 16. 
#
# In addition, python is very much general purpose. As such, there may be some relatively unexpected behavior. In python, you can define lists as such x = [1,2,3]. But the behavior of these lists can be unexpected.

[2,3,4] * 3

# Thats right - this 'multiplies' the list by three - i.e. it repeats the list three times. Not exacly expected or (for a statistician) usefull. 
#
# Python people are smart - one of the most common libraries is called numpy which defines a powerful set of classess that are useful for quantitative scientists. Possibly the most used is called a numpy array that allows vectors, matricies, and n-dimensional arrays to act much more tamely for data scientists - We will cover these in a bit. 

import numpy as np
x = np.array([2,3,4])

# If you have Googled 'python for data science' or something similar, you've probably heard of numpy, a library that provides array and matrix functionality to python. These are very important, but in my opinion, fairly low level for beginners, so we will tackle those later.


