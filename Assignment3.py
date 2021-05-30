
# # ************************  Problem - 1  **********************           # solved
# # Write a Python program to count the number of characters (character frequency) in a string.

# x=list(input("Enter a string:"))
# print(x,len(x))
# temp=[]
# for i in range(len(x)):
#     #print(i)
#     if x[i] in temp:
#         continue
#     else:
#         temp.append(x[i])
#         # print(temp)
#         y=x.count(x[i])    
#     print(f"{x[i]}:{y}")




# # ************************  Problem - 2  **********************        #solved
# # Write a Python program that accepts a comma separated sequence of words as input and 
# # prints the unique words in sorted form (alphanumerically)

# x=input('Enter number of words using comma:')
# a=x.split(',')          # all split values return to a list
# a.sort()
# for i in range(len(a)):
#     print(f'{a[i]}',end=", ")   
#     if(i==len(a)-1):
#         print("\b\b ")


# ************************  Problem - 3  **********************        #solved
#Write a Python code to remove all characters except a specified character in a given string.
# Original string
# Python Exercises
# Remove all characters except P in the said string:P

# word=input("Enter a string:")
# sp_ch=input("Enter a specified character:")
# a=len(word)
# i=0
# while(a!=0):
#     if(sp_ch==word[i]):
#         print(word[i],end="")
#     i +=1
#     a -=1

# or in a very simple way
# x=word.count(sp_ch)
# print(sp_ch*x)



# # ************************  Problem - 4  **********************                #solved
# # Write a Python program to remove an empty tuple(s) from a list of tuples   
# # Sample data: [(), (), ('',), ('a', 'b'), ('a', 'b', 'c'), ('d')]
# # Expected output: [('',), ('a', 'b'), ('a', 'b', 'c'), 'd']

# x_list=[(), (), ('',), ('a', 'b'),(), ('a', 'b', 'c'), ('d'),(),()]
# print("\n",x_list)
# y_list=[]
# #print(x_list[0],type(x_list[0]),len(x_list[0]))
# #print(x_list[4],type(x_list[4]),len(x_list[4]))

# for i in range(len(x_list)):
#    # print(x_list[i],len(x_list[i]))
#     if(len(x_list[i])!=0):
#         y_list.append(x_list[i])
# print(y_list)



#*************
numbers = [1,2,3,4]
letters = ['a','b','c','d']
zipped = zip(numbers,letters)
print(zipped)           # o/p is <zip object at 0x000000E6C3C79500>
print(type(zipped))     # <class 'zip'>
print(list(zipped))     # [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]


