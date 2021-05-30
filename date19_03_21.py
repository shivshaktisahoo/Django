'''
x=5
y=2
# ************     Arithmetic operator  *************
print(x+y)
z=x*y
print('mul =',z,'add =',(x+y),'sub =',(x-y),'div = ',(x/y),end=(' '))
print('pow =',x**y,'special division =',(x//y))


Case of Indentation ERROR in python------->
 print(x+y) 
In above line of code there is a space in frontside of print statement 

if (x>y) :
    print('x =',x,'is greater')
else :
     print("y =",y,"is greater") 


print('"hello"',end="")
print('"hello"',end="\t")
print('"hello"')

# *******************   for Input  ***********************
print('enter ur first name :')
f_name= input()
print(f_name)
l_name= input("ENTER ur last name:")
print(l_name)
print(f_name+l_name)
print(f_name,l_name)


x1=input()                  
x2=input()
print(x1,x2)
print(type(x1),type(x2))                # doubt why is it showing string if we giving integer type value

x3='abc'
x4=3
x5=455.25
x6='xyz'
x7=31
x8=405.100
print(type(x3),type(x4),type(x5))

#string 
print(x3+x6)        
#print(x3-x6)           # TypeError: unsupported operand type(s) for -: 'str' and 'str'
#print(x3*x6)           # TypeError: can't multiply sequence by non-int of type 'str'
#print(x3/x6)           # TypeError: unsupported operand type(s) for /: 'str' and 'str'

#float
print(x5+x8,x5-x8,x5*x8,x5//x8)

print(type(True))   
print(type(False),type(None))

#print(c2)           #NameError: name 'c2' is not defined
a,b=input("enter 1st number"),input("enter 2nd number")
print(a,b)
if(a>b):
    print("1st number =",a," is greater")
    print(f"1st number = {a} is greater")       # f ---- f string example
elif(a<b) :
    print("2nd number =",b, "is greater")
    print(f"2nd number = {b} is greater")
else:
     print("Both r Equal")

x=int(input("something:"))
print(x,type(x))
x='d'
print(f'ascii value of d is {ord(x)}')
z=int(ord(x)/ord(x))
print(z)
for i in range(z,ord(x)+z):
    print(f'{i}',end=" ")

'''
word='word'
sentence="This is the sentence."
paragraph="""This is a paragraph. It is made up of multiple lines and sentences"""
print(word,sentence,paragraph)