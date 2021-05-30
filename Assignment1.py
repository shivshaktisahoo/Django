# 50
# 620
# # *********************** Problem - 1 ****************************          # solved
# # Ask subject marks from user and 
# # display him total, percentage, grade ( pass,1st Division, 2nd Division or Distinction)

# y=0
# for i in range(5) :
#     x=float(input(f"Enter your mark for subject{i+1} = "))
#     y=y+x
# p=(y/500.0)*100 
# print(f"Your Total marks is {y} \t Percentage is {p} \t Grade is ",end="")
# if(p>=60.0):
#     print('"1st division"')
# elif(p>=50.0):    
#     print('"2nd division"')
# elif(p>=35.0):
#     print('"3rd division"')
# else:
#     print('"FAIL"')     


# # *********************** Problem - 2 ****************************           #  solved                             
# # Ask number from user and display Fibonacci series of that number.

# n=int(input("\nEnter your number for fibbonaci series : "))
# a,b=0,1
# print(a,b,end=" ")
# for i in range(n-2):
#     c=a+b
#     a=b
#     b=c
#     print(c,end=" ")          
            
                                   
  

# # *********************** Problem - 3 ****************************           #  solved
# # Ask number from user and display if it is a prime/odd/Even number.
# x = int(input("\nEnter a Number(Even/odd/prime) = "))
# y=x%2;count=0
# if(y==0):
#     print(f'{x} is an Even Number')
# else:    
#     print(f'{x} is an Odd Number',end=" ")
# for i in range(2,x):
#     if((x%i)==0):   
#         count +=1
# if(count==0):
#     print('and a prime number')
# else:
#     print('and a non-prime number')




# # *********************** Problem - 4 ****************************           # solved
# # Write a Python program which accepts the radius of a circle from the user and compute the area.
# # Sample Output :
# # r = 1.1
# # Area = 3.8013271108436504

# r=float(input("Enter a Radius of a Circle = "))
# a=(22/7)*r*r
# print('AREA of Cirlce is ',a)



# # *********************** Problem - 5 ****************************           # solved
# # Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

# print('Enter 3 integers:')
# x,y,z=int(input("x : ")),int(input("y : ")),int(input("z : "))
# if(x==y or y==z or x==z):
#     print('Sum is 0')
# else:
#     sum=x+y+z
#     print(f'sum is {sum}')


# # *********************** Problem - 6 ****************************           # solved
# # Write a Python program to compute the distance between the points (x1, y1) and (x2, y2).
# print('Enter 1st point')
# x1,y1=float(input("x1 : ")),float(input("y1 : "))
# print('Enter 2nd point')
# x2,y2=float(input("x2 : ")),float(input("y2 : "))
# d=((x2-x1)**2+(y2-y1)**2)**(1/2)
# print(f'The Distance between 2 points is {d} unit')


# # *********************** Problem - 7     ****************************        #  solved
# # Write a Python program to test whether a number is within 100 of 1000 or 2000.
# # Mean a number is close by at least 100 to 1k or 2k

# n=float(input("Enter the Number : "))
# a=2000-n
# b=1000-n
# if(0<a<100) or (0<b<100):
#     print("in between 100")
# else:
#     print("outside 100")



# # *********************** Problem - 8 (GCD) **************************        #  solved 
# # Write a Python program to compute the greatest common divisor (GCD) of two positive integers 
# print('Enter 2 Numbers:')
# x,y=int(input("x : ")),int(input("y : "))
# #print(x,y)                                      
# iterat=0
# hcf=0
# if(x<y):
#     iterat=x
# else:
#     iterat=y
# for i in range(1,iterat+1):
#     if(x%i==0)and(y%i==0):
#         #print("factors are ",i)
#         if hcf<i:
#             hcf=i
# print(f"GCD of {x} and {y} is {hcf}")



# *********************** Problem - 9 (LCM) ****************************      #  solved  
# Write a Python program to get the least common multiple (LCM) of two positive integers.
print('Enter 2 Numbers:')
x,y=int(input("x : ")),int(input("y : "))
print(x,y)
#x=3
#y=7
count=0
lcm=0
iterat=0
if x>y:
    iterat=x
else:
    iterat=y
if (iterat%x==0) and (iterat%y==0):
    print(f"LCM of {x} and {y} is {iterat}")
else:
    for i in range(iterat,((x*y)+1)):
        if (i%x==0) and (i%y==0):
            #print("LCM is",i)
            count +=1
           # print(count) 
            if(count==1):
                lcm=i
        # i +=1
    print(f"LCM of {x} and {y} is {lcm}")








