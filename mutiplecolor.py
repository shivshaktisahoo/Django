import matplotlib.pyplot as plt

x = [i for i in range(0,10)]
y = [i**3 for i in range(0,10)]

for i in range(len(x)):
    plt.scatter(x[i],y[i])
plt.show()