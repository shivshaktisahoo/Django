import pandas as pd
import numpy as np
import sklearn 
from sklearn import model_selection


data = pd.read_csv('https://raw.githubusercontent.com/SujanSharma07/Machine-Learning/master/heart_disease/heart.csv')
x = data.drop(['target'], axis=1)
y = data['target']

columns = ['age', 'sex (1 for male or 0 for female)', 'cp (0 to 4)', 'trestbps', 'chol', 'fbs', 'restecg',
       'thalach', 'exang', 'oldpeak', 'slope', 'ca', 'thal']
output = ['NO Heart Diseases',' Risk of Heart Disease ']


x_train, x_test, y_train, y_test =  sklearn.model_selection.train_test_split(x,y,test_size=0.1)

from sklearn.tree import DecisionTreeClassifier,DecisionTreeRegressor
reg = DecisionTreeClassifier()

reg.fit(x_train,y_train)

reg.score(x_test,y_test)

data = []
for i in columns:
  data.append(int(input(f"Enter the value of {i}:")))

data = np.array(data).reshape(1,-1)
print(output[reg.predict(data)[0]])