# ***********Assignment-heartdieaseschart**********
import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv('https://raw.githubusercontent.com/SujanSharma07/Machine-Learning/master/heart_disease/heart.csv')
# male_hd = data.loc[(data['sex']==1) & (data['target']==1)].count()["age"]
# female_hd = data.loc[(data['sex']==0) & (data['target']==1)].count()["age"]
# total_male = data.loc[(data['sex']==1)].count()['sex']
# total_female = data.loc[(data['sex']==0)].count()['sex']
# y = [(male_hd/total_male)*100,(female_hd/total_female)*100]
# x = ['Male','Female']

# plt.bar(x,y,width=0.5)
# plt.title("Heart Dieases prediction Chart :",color="Red",size=20)
# plt.xlabel("Categories--------->",color="Blue",size=15)
# plt.ylabel("Chances(in %)--------->",color="Green",size=15)
# plt.show()


hd_male = data.loc[(data['sex']==1) & (data['target']==1)].count()["age"]
hd_female = data.loc[(data['sex']==0) & (data['target']==1)].count()["age"]
total_male = data.loc[(data['sex']==1)].count()['sex']
total_female = data.loc[(data['sex']==0)].count()['sex']
y = [(hd_male/total_male)*100,(hd_female/total_female)*100]
x = ['Male','Female']
plt.pie(y,labels=x,autopct="%1.2f%%")
# plt.bar(x,y,width=0.5)
plt.title("Heart Dieases Chances (w.r.t Gender) :",color="Red",size=20)
# plt.xlabel("Categories--------->",color="Blue",size=15)
# plt.ylabel("Chances(in %)--------->",color="Green",size=15)
plt.gca().legend(loc='center left', bbox_to_anchor=(1, 0.5))        # outside the plot
plt.show()