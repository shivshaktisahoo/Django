# ***************************** Problem-1 : ********************************** # solved
# ***************************** BANK_APPLICATION *****************************
import ast
class Bank:
    def __init__(self):
        pass

    # User login Function/method
    def signin(self):
        account_id = input(" Enter Your ID/Name ")
        account_pwd = str(input(" Enter Your password: "))
        decison = check_id(account_id,account_pwd)
        x=account_id
        if decison == None:
            x,decison = check_name(account_id,account_pwd)                      # here x is the id
        if decison != None:
            print("We have this account ",decison)
            while(True):
              n = str(input('For DEPOSIT :   type 1\nfor WITHDRAW :  type 2\nfor EXIT:\ttype 0\n'))
              if (n=='1'):
                self.deposit(x)                                                       # here x is the id
              elif (n=='2'):
                self.withdraw(x)
              elif (n=='0'):
                print("**************** Have a Nice Day!!! ********************   ")
                break
              else:
                print('enter correct keyword')
        else:
            print("No such Account")

    # New User Signup Function/method
    def signup(self):
        global d1
        sub_d1 = dict()
        id = max(d1['detail'].keys()) + 1
        sub_d1["Name"] = input('Enter ur name : ')
        sub_d1['Balance'] = 0
        d1['detail'][id] = sub_d1
        d1['auth'][id] =  input('Enter new PIN : ')   
        with open('demo.txt','w') as file1:
             file1.write(str(d1))
        print(f"New Account Created\nId : {id}\nName : {d1['detail'][id]['Name']}\nBalance : {d1['detail'][id]['Balance']}\nPIN : {d1['auth'][id]}\n")
        return d1
    
    def deposit(self,id):                                       # for deposit and updating Balance
        global d1
        id= int(id)
        amount = int(input('Enter deposit amount : '))
        d1['detail'][id]['Balance'] += amount
        print(d1['detail'][id])
        with open('demo.txt','w') as file1:
            file1.write(str(d1))

    def withdraw(self,id):                                  # for withdrawing and updating Balance
        global d1
        id = int(id)
        amount = int(input('Enter withdraw amount   : '))
        if (d1['detail'][id]['Balance']>=amount):
            d1['detail'][id]['Balance'] -= amount
            print(d1['detail'][id])
        else:
            print('You Have Insufficiant Balance!!!! ')
        with open('demo.txt','w') as file1:
           file1.write(str(d1))



# Checking Name and pasword entered by user is correct or not
def check_name(name,pwd):
    for id, details in d1['detail'].items():
        try:
            if (d1['detail'][id]['Name']).lower() == name.lower():
                if(pwd==d1['auth'][id]):
                    return id,details
                else:
                    print('Wrong Password')     
        except:
            pass
    else:
        return id,None

# Checking ID and pasword entered by user is correct or not
def check_id(id,pwd):
    try:
        id = int(id)
        if (pwd==d1['auth'][id]):
            acc_detail = d1['detail'][id]
            return acc_detail
        else:
            print('Wrong Password')    
    except:
        return None


with open('demo.txt','r') as file1:
    i = file1.read()
    i = ast.literal_eval(i)                    # i = eval(i), it is more risky              #converted string to dictinory
d1 = dict(i)
while(True):
    print('\n******************** Welcome To ABC Bank **************************' )
    log = input('For SIGNIN :   type 1\nfor SIGNUP :   type 2\n')
    x = Bank()      # x is a object of Bank class
    if log == '1':
        x.signin()
        break
    elif log == '2':
        x.signup()
        continue
    else:
        print('press correct keyword')



# ***************************** Problem-2: *********************************    # solved
# 2: Write a Python program where you take any positive integer n, if n is even, divide
# it by 2 to get n / 2. If n is odd, multiply it by 3 and add 1 to obtain 3n + 1. Repeat the
# process until you reach 1.
# Input : 12
# Output : [12, 6.0, 3.0, 10.0, 5.0, 16.0, 8.0, 4.0, 2.0, 1.0]
def conjecture(p_num):
    list1 = [p_num]
    while (p_num!=1):
        if p_num%2==0:
            p_num //= 2   
        else:
            p_num = 3*p_num+1
        list1.append(p_num)
        continue
    return list1
p_num = int(input("Enter a positive integer: "))
print(conjecture(p_num))


# ***************************** Problem-3: *********************************    # solved
# 3: Write a Python program to check if a given string is an anagram of another given string.
# Input : 'anagram', 'nagaram'
# Output : True

def str_anagram(str1,str2):
    l1 = list(str1)
    l2 = list(str2)
    l1.sort()
    l2.sort()
    if  l1 == l2:
        return True
    else:
        return False

str1 = input("Enter a word: ")
str2 = input("Enter another word: ")
print(str_anagram(str1,str2))


# ***************************** Problem-4: *********************************    # solved
# 4: Write a Python program to find the length of the last word.
# Input : Python Exercises
# Output : 9

def len_lastword(str1):
    list1 = str1.strip().split(" ")
    word_len = len(list1[-1])
    return word_len

str1 = input("Enter a word or sentence: ")
print(len_lastword(str1))
