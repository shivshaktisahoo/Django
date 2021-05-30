import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_csv('https://raw.githubusercontent.com/SujanSharma07/Machine-Learning/master/heart_disease/heart.csv')

age_below20 = data.loc[data['age']<=20].count()['age']
age_20_40 = data.loc[(data['age']>20) & (data['age']<=40)].count()['age']
age_40_60 = data.loc[(data['age']>40) & (data['age']<=60)].count()['age']
age_60_80 = data.loc[(data['age']>60) & (data['age']<=80)].count()['age']
age_above80 = data.loc[data['age']>80].count()['age']

x = ["0-20","20-40","40-60","60-80","80+"]
y = np.array([age_below20,age_20_40,age_40_60,age_60_80,age_above80])
plt.bar(x,y)
plt.title("Age catogeries Chart :",color="Red",size=30)
plt.xlabel("Age-------->",color="Blue",size=20)
plt.ylabel("No.of peoples--------->",color="Green",size=20)
plt.show()

# count without count method
age_50 = data.loc[data['age']>50]
print(f'No. of people above Age_50 is {age_50.shape[0]}')

