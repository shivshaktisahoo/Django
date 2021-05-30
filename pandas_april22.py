import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Series is Sequence of data values.
# DataFrames is a tablular form where as series is list form
# data = [10,25,12,45,46]
# data1 = pd.Series(data)
# print(data1)
# print(type(data1))      #O/P is  <class 'pandas.core.series.Series'>
# print(data1[0])
# data1 = pd.Series(data,index=['Hours','History','English','Rohit','Shiv'])
# print(data1)            # instead of 0,1,2,3,4,5 the values of index with print 
# print(data1["Hours"])   # and we can access data with by indexing them
# # or
# print(data1[0])

# #DataFrame
# data = {'Name':['Shiv','Rohit'],'Age':[67,76]}
# data1 = pd.DataFrame(data)
# print(data1['Name'],type(data1['Name']))        
# data = {'Name':['Shiv','Rohit'],'Age':[67,76]}
# data1 = pd.DataFrame(data,index=['person','mood'])
# print(data1)                        # A table 
# print(type(data1))                  # <class 'pandas.core.frame.DataFrame'>

#File Handling::
# this is a link of a CSV file
# https://raw.githubusercontent.com/SujanSharma07/Machine-Learning/master/heart_disease/heart.csv
data = pd.read_csv('https://raw.githubusercontent.com/SujanSharma07/Machine-Learning/master/heart_disease/heart.csv')
# print(data)
# print(data.head())      # shows top 5 table(by_default) from UPPER of that CSV file
# print(data.head(10))     # desired table we want like 10 tables
# print(data.tail())      # shows last 5 table(by_default) from BOTTOM of that CSV file
# print(data.tail(10))     # desired table we want like 10 tables

# print(data.to_string())

# print(data.shape)   # show you how many rows and columns that DataFrame has
# print(data.size)    # Totalnumber of values you are dealing with i.r row*column

# print(data['target'])
# print(type(data))
# print(data.iloc[0])
# print(data.head())
# print(data.iloc[1])
# print(data.loc[1,'age'])
# print(data.iloc[5:100])




# age_below20 = data.loc[data['age']<=20].count()['age']
# print(age_below20)
# age_20_40 = data.loc[(data['age']>20) & (data['age']<=40)].count()['age']
# print(age_20_40)
# age_40_60 = data.loc[(data['age']>40) & (data['age']<=60)].count()['age']
# print(age_40_60)
# age_60_80 = data.loc[(data['age']>60) & (data['age']<=80)].count()['age']
# print(age_60_80)
# age_above80 = data.loc[data['age']>80].count()['age']
# print(age_above80)
# x = ["0-20","20-40","40-60","60-80","80+"]
# y = np.array([age_below20,age_20_40,age_40_60,age_60_80,age_above80])



# # count without count method
# age_20_40 = data.loc[(data['age']>20) & (data['age']<=40)]
# print(age_20_40.shape[0],type(age_20_40))
# age_40_60 = data.loc[(data['age']>40) & (data['age']<=60)]
# print(age_40_60.shape[0],type(age_40_60))

# ***********Assignment-heartdieaseschart**********
male_hd = data.loc[(data['sex']==1) & (data['target']==1)].count()["age"]
female_hd = data.loc[(data['sex']==0) & (data['target']==1)].count()["age"]
total_male = data.loc[(data['sex']==1)].count()['sex']
total_female = data.loc[(data['sex']==0)].count()['sex']
y = [(male_hd/total_male)*100,(female_hd/total_female)*100]
x = ['Male','Female']
plt.bar(x,y,width=0.5)
plt.title("Heart Dieases prediction Chart :",color="Red",size=20)
plt.xlabel("Categories--------->",color="Blue",size=15)
plt.ylabel("Chances(in %)--------->",color="Green",size=15)
plt.show()