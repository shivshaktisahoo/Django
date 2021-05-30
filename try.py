'''
#file1=open('demo.txt','w')
#file1.write('Hello Shiv')
#file1.close()

list_x  = ['Happy To see you\n','Rohit\n','Shiv \n']
# write and writelines
with open('demo.txt','w') as file:
    for i in range(10):
        x='*'*i
        file.write(x)
        file.write('\n')
    file.writelines(list_x)

#read and readlines
with open('demo.txt','r') as file:
    #for i  in file.read():
    #    print(i)
    for i in file.readlines():
        print(i,end='')


#append
with open('demo.txt','a') as file:
    for i in range(10):
        x='*'*i
        file.write(x)
        file.write('\n')


with open('demo.txt','r') as file:
    #print(len(file.read()))
    for i in file.read():
        if(i==','):
            print('\n')
        else:
            print(i,end='')

'''

detail = {123: {'Name': "Rohit", "Balance": 14000},
          111: {'Name': "Shiv", "Balance": 100},
          177: {'Name': "Deepesh", "Balance": 1000000},
          }
y = detail[111]
i = y['Balance'] + 2000
print(i)
# ask id from user and manipulate that part only
#provide