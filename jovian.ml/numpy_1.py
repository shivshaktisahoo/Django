import numpy as np
import urllib.request               # requesting document download

urllib.request.urlretrieve('https://hub.jovian.ml/wp-content/uploads/2020/08/climate.csv','E:\python\jovian.ml/climate.txt')

climate_data = np.genfromtxt('climate.txt',delimiter=',',skip_header=1)     # path name for a file, delimiter is used to by which seperation will be done(by , or as in file it can be :, etc..)
# and to skip the header in line 1 as it contains(temerature, rainfall, humidity)   
# np.genfromtxt() is used create in array object from a text file
print(climate_data) 
weigths = np.array([0.3,0.2,0.5])
yields = climate_data @ weigths     # In numpy,  @ means matrix multiplication
print(yields)
print(yields.shape)
climate_results = np.concatenate((climate_data, yields.reshape(10000,1)), axis=1 )
# concatenate other matrix with an existing matrix
print(climate_results)

# to save in a file(or different file)
np.savetxt('climate_results.txt',
            climate_results,
            fmt='%.2f',
            header='temperature,rainfall,humidity,yields_apples',
            comments='') 