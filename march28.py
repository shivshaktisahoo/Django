'''
shiv_dic = {
    "Name": "Shiv Shakti",
    "Age": 34,
    "Marks": {"Maths": 45,'Science': 56, 'Computer': 98},
    "phn_no": [98823098,78273987,289734],
    }
print(shiv_dic)
print(shiv_dic["Age"])
print(shiv_dic["Marks"])
print(len(shiv_dic))
for i in shiv_dic:
    print(i)
print(shiv_dic.keys())
for i in shiv_dic:
    print(shiv_dic[i])

print(shiv_dic.values())
print(shiv_dic.items())
n_dic=shiv_dic["Marks"]
print(n_dic)
print(n_dic.values())
sum=0
for i in n_dic.values():
    sum +=i
print(sum)

#exception Handling
try:
    x=int(input('Enter your Age :'))
    print('Age = ',x)
except:
    print('Please enter correct value')

while(True):
    try:
        x=int(input('Enter your Age :'))
        print('Age = ',x)
        break
    except:
        print('Please enter correct value')
        

word="shiv"
for i in word:
    print(i)


l1 = ['b','c','d','e','f']
for i in range(len(l1)):
    for j in range(i+1,len(l1)):
        print(l1[i],l1[j])


balance =10000
l1=[1000,2000,3000]
def withdrawl(x):
    global balance
    balance -= x
    print('After withdrawl you have balance : ', balance)

def deposit(x):
    global balance
    balance += x
    print('After deposit you have balance : ', balance)

def add(x):
    sum = 0
    for i in x:
        sum +=i
    return sum

withdrawl(1000)
deposit(5000)

d1={'rohit': 98,'shiv':89,'deepak':100}
d2={'mohit': 92,'raj':91,'deepun':90}
print(d1,d2)
for (i,j),(a,b) in zip(d1.items(),d2.items()):
    print(i,j)
    print(a,b)



def hello_master(func):
    print('I am in master')
    return func()                 #u have to pass function
def hello_slave():
    print('I am in Slave')

hello_master(hello_slave)

def hello_master1(func):
    print('I am in master1')
    return func()                #u have to pass function
@hello_master1                      # this done to execute first and then slave1
def hello_slave1():
    print('I am in Slave1')

hello_slave1


# r = Read, w = Write, a = Append
#file1 = open('demo.txt', 'w')
#file1.write(" Hello Rohit ")
#file1.close()

# write and writelines

list_x = ['Happy to see you\n',
          'Rohit are you done?\n', 'Hello Shiv.. Okay\n']

with open('demo.txt', 'w') as file1:
    for i in range(10):
        x = '*'*i
        file1.write(x)
        file1.write('\n')
    file1.writelines(list_x)


# read and readline
with open('demo.txt', 'r') as file1:
    for i in file1.readlines():
        print(i,end='')



# append
with open('demo.txt', 'a') as file1:
    for i in range(10):
        x = '*'*i
        file1.write(x)
        file1.write('\n')



def deposite(x, y):
    print(f"New Balance of {y} deposited")
    return x+y


def withdraw(x, y):
    print(f"Balance {y} withdraw")
    return x-y


with open('demo.txt', 'r') as file:
    x = int(file.readline())
    print("You have balance ", x)
    decison = int(input("Press 1 to deposite and 2 to withdraw"))
    if decison == 1:
        amount = int(input(" Enter the amount you want to deposite "))
        y = deposite(x, amount)
    else:
        amount = int(input(" Enter the amount you want to withdraw "))
        y = withdraw(x, amount)

    with open('demo.txt', 'w') as file2:
        file2.write(str(y))

'''
# ask id from user and manipulate that part only
# Provide Choice whether user want to choose account on the basis of account no or name of av=ccount holder
# after account is choosed manipulation obtions like deposite  and withdrawl

auth = {123:"123",
        111:"111",
        177:"177"}
        
detail = {123: {'Name': "rohit", "Balance": 14000},
          111: {'Name': "shiv", "Balance": 100},
          177: {'Name': "deepesh", "Balance": 1000000},
          }
# for id, details in detail.items():
#     print(id,details)

def check_name(name,pwd):
    for id, details in detail.items():
        try:
            if details['Name'] == name.lower():
                if(pwd==auth[id]):
                    return details
                else:
                    print('Wrong Password')      
        except:
            pass
    else:
        return None

def check_id(id,pwd):
    try:
        id = int(id)
        if(pwd==auth[id]):
            acc_detail = detail[id]
        else:
            print('Wrong Password')
        return acc_detail
    except:
        return None

account_id = input(" Enter Your ID/Name ")
account_pwd = str(input(" Enter Your password: "))
decison = check_id(account_id,account_pwd)


if decison == None:
    decison = check_name(account_id,account_pwd)
    print('line1')

if decison != None:
    print("We have this account ", decison)
else:
    print("No such Account")


