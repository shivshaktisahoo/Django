# # ***************************** Problem - 1 ****************************        # solved
# for i in range(6):
#     for j in range(i):
#         print('*',end=" ")
#     print('')
# for i in range(4,0,-1):
#     for j in range(i):
#         print('*',end=' ')
#     print('')



# # ***************************** Problem - 2 ****************************        # solved

# data=str(input('Enter  a  Word  : '))
# #print(data)
# x=len(data)
# #print(x)
# print('Reverse of Word :',end=' ')
# for i in range(x-1,-1,-1):
#     print(data[i],end='')

# #or we can do in this trick
# print("\n",data[::-1])

#***************************** Problem - 3 ****************************        # solved   
n=int(input('\nEnter a Number : '))
order=len(str(n))
#print(n,type(n))
a=n
sum=0
while(a!=0):
    x=a%10
    a=a//10
    sum +=(x**order)
   # print(x,a,sum)
#print(sum)
if(n==sum):
    print(n," is an Armstrong Number")
else:
    print(n," is not an Armstrong Number")
    
# # ***************************** Problem - 4 ****************************        # solved
# for i in range(10):              
#     for j in range(i):
#         print(i,end="")
#     print(' ')

# #(OR can be done in this way)      output will be same as (string * integer) gives that no. of string
# for i in range(10):                           
#     print(str(i)* i)                # a*2=aa, a*3=aaa





