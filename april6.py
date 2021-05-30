# ask id from user and manipulate that part only
# Provide Choice whether user want to choose account on the basis of account no or name of acccount holder
# after account is choosed manipulation options like deposite  and withdrawl
with open('demo.txt','r') as file1:
    i=file1.read()
    i=eval(i)
d1=dict(i)

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

def check_id(id,pwd):
    try:
        id = int(id)
        if(pwd==d1['auth'][id]):
            acc_detail = d1['detail'][id]
            return acc_detail
        else:
            print('Wrong Password')
        
    except:
        return None

def deposit(id):
   global d1
   id= int(id)
   amount = int(input('Enter deposit amount : '))
   d1['detail'][id]['Balance'] +=amount
   print(d1['detail'][id])
   with open('demo.txt','w') as file1:
       file1.write(str(d1))

def withdraw(id):
   global d1
   id= int(id)
   amount = int(input('Enter withdraw amount   : '))
   d1['detail'][id]['Balance'] -=amount
   print(d1['detail'][id])
   with open('demo.txt','w') as file1:
       file1.write(str(d1))

account_id = input(" Enter Your ID/Name ")
account_pwd = str(input(" Enter Your password: "))
decison = check_id(account_id,account_pwd)
x=account_id
if decison == None:
    x,decison = check_name(account_id,account_pwd)
if decison != None:
    print("We have this account ",decison)
    while(True):
      n=str(input('For DEPOSIT :   type 1\nfor WITHDRAW :  type 2\nfor EXIT:\ttype 0\n'))
      if (n=='1'):
        deposit(x)
        break
      elif (n=='2'):
        withdraw(x)
        break
      elif (n=='0'):
        print("**************** Have a Nice Day!!! ********************   ")
        break
      else:
        print('enter correct keyword')
else:
    print("No such Account")