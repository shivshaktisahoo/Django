# ***********Assignment-heartdieaseschart**********
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('https://raw.githubusercontent.com/SujanSharma07/Machine-Learning/master/heart_disease/heart.csv')
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