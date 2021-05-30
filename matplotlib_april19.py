import matplotlib.pyplot as plt
import numpy as np

x = np.array([1,2,3,4,5,6])
y = np.array([1,4,9,16,25,36])
# (1,1),(2,4),(3,9),(4,16),(5,25),(6,36)
plt.plot(x,y)
plt.title("Squares Chart")
plt.xlabel("Numbers")
plt.ylabel("sqaure")
plt.show()                  # shows above plot(x,y)


#!nvidia-smi

x1 = [1,2,3,4,5,6]
y1 = [45,67,886,54,343,443]

# 00000000 - 11111111 = 2^8 = 256 --> 0 - 255
# (1,1),(2,4),(3,9),(4,16),(5,25),(6,36)
#color = (R,G,B)
#plt.plot(x,y,color=(255/255,0/255,0/255))
plt.plot(x1,y1,color=(1,1,0))       # shows colour as per desired we can do with also 'c' instead of 'color'
# color in percentage,it can be used in hexadecimal colour--> '#aaffee'  or with name "red",'yellow' 
plt.title("Growth Rate",color=(.3,.5,0.7))
plt.xlabel("Age",c='#ae4210')
plt.ylabel("Height",c='Red')
plt.show()



# plotting multiple lines in a single graph or figure
x = [1,2,3,4,5,6]
y = [1,4,9,16,25,36]

x1 = [i for i in range(0,5)]
y1 = [i**3 for i in range(0,5)]
y3 = [i for i in range(10)]

plt.plot(x,y,color=(1,1,0))
plt.plot(x1,y1,color=(0,0,1))
plt.plot(y3,c="hotpink")
plt.title("Growth Rate")
plt.xlabel("Age")
plt.ylabel("Height")
plt.show()



# scatter points for each elements of two points  
# and multiple scatter points in single graph or figure
x = [1,2,3,4,5]
y = [1,4,9,16,25]

x1 = [i for i in range(0,5)]
y1 = [i**3 for i in range(0,5)]

# 00000000 - 11111111 = 2^8 = 256 --> 0 - 255
# (1,1),(2,4),(3,9),(4,16),(5,25),(6,36)
#color = (R,G,B)
#plt.plot(x,y,color=(255/255,0/255,0/255))
plt.scatter(x,y,color=(1,1,0))
plt.scatter(x,y1,color="#fe19ac")
plt.scatter(x,x1,c='aquamarine')
plt.plot(x1,y1,color=(0,0,1))

plt.title("Growth Rate")
plt.xlabel("Age")
plt.ylabel("Height")
plt.show()



#**************************************************
x = [1,2,3,4,5]
y = [1,4,9,16,25]

x1 = [i for i in range(0,5)]
y1 = [i**3 for i in range(0,5)]

# 00000000 - 11111111 = 2^8 = 256 --> 0 - 255
# (1,1),(2,4),(3,9),(4,16),(5,25),(6,36)
#color = (R,G,B)
#plt.plot(x,y,color=(255/255,0/255,0/255))
plt.plot(y,y1,color='#5412fe')  
plt.plot(x1,y1,'+',color=(0,0,1))              # instead of o use + for visual repersentation
plt.plot(x,y1,'o',color=(0,0,1))
plt.plot(x,x1,'s',color='hotpink',ms=10.5,mec='blue',mfc='hotpink')
#ms is markersize, mec is marker edge colour, mfc is marker face colour
plt.scatter(x,y,color=(1,1,0))
plt.title("Growth Rate",fontdict = {'family':'serif','fontsize':50,'color':'Red'})
plt.xlabel("Age")
plt.ylabel("Height")
plt.show()


# y = np.array([3,5,7,9,1,4,6])
# plt.plot(y,linewidth='12')
# plt.grid()
# plt.show()


# y = np.array([3,5,7,9,1,4,6])
# plt.plot(y,linewidth='12')
# plt.grid()
# plt.show()

# #x ,y, x1, y1
# x = [1,2,3,4,5,6]
# y = [1,4,9,16,25,36]

# x1 = [i for i in range(0,5)]
# y1 = [i**3 for i in range(0,5)]
# plt.subplot(2,2,2)
# # 2 rows 2 columns 2 position
# plt.plot(x,y)

# plt.subplot(2,2,3)
# plt.plot(x1,y1)

# #Bars

# #x ,y, x1, y1
# x = [1,2,3,4,5,6]
# y = [1,4,9,16,25,36]

# x1 = [i for i in range(0,5)]
# y1 = [i**3 for i in range(0,5)]
# plt.subplot(2,2,2)
# # 2 rows 2 columns 2 position
# plt.plot(x,y)

# plt.subplot(2,2,3)
# plt.plot(x1,y1)

# x = np.array(['Python','Java','R','Ruby','JS'])
# y = np.array([88,45,78,32,86])
# plt.bar(x,y,color=(1,1,0))
# plt.show()

# x = np.array(['Python','Java','R','Ruby','JS'])
# y = np.array([88,45,78,32,86])
# plt.bar(x,y,width=0.2)
# plt.show()

# x = np.array(['Python','Java','R','Ruby','JS'])
# y = np.array([88,45,78,32,86])
# plt.barh(x,y)
# plt.show()

# x = np.array(['Python','Java','R','Ruby','JS'])
# y = np.array([10,5,8,3,8])
# plt.barh(x,y,height=0.2)
# plt.show()

# #Pie Chart\\
# x = np.array(['Python','Java','R','Ruby','JS'])
# y = np.array([88,45,78,32,86])
# total = y.sum()
# percentage = ((y/total)*100)
# degree = percentage*360/100
# degree.sum()

# plt.pie(y,labels=x)
# plt.show()

# plt.pie(y,labels=x, explode=(0,0,.3,0,.1))
# plt.show()

# x = np.array(['Python','Java','R','Ruby','JS'])
# y = np.array([88,45,78,32,86])
# total = y.sum()
# percentage = ((y/total)*100)
# degree = percentage*360/100
# percentage

# plt.pie(y, labels = x,explode=(.2,.1,.3,.1,.1), autopct="%1.2f%%")
# plt.show()

# plt.pie(y, labels = x,explode=(.2,.1,.3,.1,.1), autopct="%1.0f%%")
# plt.show()

# x = [1,2,3,4,5,6]
# y = [1,4,9,16,25,36]

# x1 = [i for i in range(0,5)]
# y1 = [i**3 for i in range(0,5)]

# # 00000000 - 11111111 = 2^8 = 256 --> 0 - 255
# # (1,1),(2,4),(3,9),(4,16),(5,25),(6,36)
# #color = (R,G,B)
# #plt.plot(x,y,color=(255/255,0/255,0/255))
# for i in range(len(x)):
#   t = (i/10) + 0.4
#   w = (i/15) + 0.056

#   plt.scatter(x[i],y[i],color=(t,0,w))

# plt.title("Growth Rate")
# plt.xlabel("Age")
# plt.ylabel("Height")
# plt.show()