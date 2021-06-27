# -*- coding: utf-8 -*-
"""Shiv_linearregression(9th june).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1g-7-Wr-Ruh_6wcqYP8wB7Q17m4oR6tU8

Linear Regression questions
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (10,5)

dataset = pd.read_csv("https://raw.githubusercontent.com/shivshaktisahoo/test/main/salaries.csv")
dataset

"""## 1. Find Mean of X, Y"""

x = dataset['Years of Experience'].mean()
y = dataset['Salary'].mean()
print(f"Mean of Years of Experience is {x}\nMean of Salary is {y}")

"""## Display data in graph"""

x = dataset['Years of Experience']
y = dataset['Salary']
plt.scatter(x,y,linewidth=1)
plt.title("Salaries  Chart :", color="Red", size=20)
plt.xticks(size=12)
plt.yticks(size=12)
plt.xlabel("Years of Experience -------->",c='Brown', size=15)
plt.ylabel("Salary (in $)--------->",c='Brown', size=15)
plt.grid()
plt.show()

"""## Analysis that you made on the data"""

print(dataset.shape)
print(dataset.size)

dataset.describe()

dataset.info()

dataset.min()

dataset.max()

"""1. With increasing in years of experience, salary is increasing almost linearly.
2. Deviation in salary with respect to experience is very less.
3. The shape of dataset is (30, 2).
4. Total number of Entries in a dataset is 30. 
5. Minimum Salary is 37731.00.
6. Maximum Salary is 122391.00.

## plot a line on the graph of data (min to max)
"""

x = dataset['Years of Experience']
y = dataset['Salary']
a = [x[0],x[x.count()-1]]
b = [y[0],y[y.count()-1]]
plt.plot(a,b,color="green")
plt.scatter(x,y,linewidth=1)
plt.title("Salaries  Chart :", color="Red", size=20)
plt.xticks(size=12)
plt.yticks(size=12)
plt.xlabel("Years of Experience -------->",c='Brown', size=15)
plt.ylabel("Salary (in $)--------->",c='Brown', size=15)
plt.grid()
plt.show()