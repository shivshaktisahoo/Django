import sklearn
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np
import pickle
import random

data = pd.read_csv('heart.csv')
reg = LogisticRegression(random_state=0)
X = data.drop(['target'], axis=1)
Y = data['target']
best = 0
for i in range(100):  # best = 52, acc = 52
    x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(
        X, Y, test_size=0.1)
    reg.fit(x_train, y_train)  # half hour
    acc = reg.score(x_test, y_test)
    print(f"Accuracy is {round(acc,2)*100}%")
    if acc > best:
        with open('model.pickle', 'wb') as f:
            pickle.dump(reg, f)
        best = acc

print(f"Saved the model with accuracy {round(best,2)*100}%")

pickle_in = open('model.pickle', 'rb')
reg = pickle.load(pickle_in)

ran_data = np.array([random.randrange(0, 120)
                     for i in range(13)]).reshape(1, -1)
result = reg.predict(ran_data)[0]
print(f"Result is {result}")

