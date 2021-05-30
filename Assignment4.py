# ***************************** Problem - 1 *****************************       #solved
#Write a Python script to print a dictionary where the keys are numbers between 1 and 15 (both included) 
# and the values are square of keys.
# Sample Dictionary
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12: 144, 13: 169, 14: 196, 15: 225}

while(True):
    try:
        n=int(input('Enter the number upto u want:'))
        break
    except:
        print('Please enter the correct value')
sq_dict={}
for i in range(1,n+1):
    sq_dict[i]=i*i
print(sq_dict)
# or
# print({i:i*i for i in range(1,n+1)})

# # ***************************** Problem - 2 *****************************       #solved
# #Write a Python program to combine two dictionary adding values for common keys.
# # d1 = {'a': 100, 'b': 200, 'c':300}
# # d2 = {'a': 300, 'b': 200, 'd':400}
# # Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})

# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d3=dict(d1)
# d3.update(d2)
# for i in d1:       
#     for j in d2:
#         if(i==j):
#             d3[i]=d1[i]+d2[j]  
# print(d3)




# # ***************************** Problem - 3 *****************************       #solved
# # Write a Python program to print all unique values in a dictionary.
# # Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# # Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}

# u_list=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
# #print(u_list)
# f_set=set()
# for i in range(len(u_list)):
#     #print(i,u_list[i])
#     for j in u_list[i]:
#         #print(u_list[i][j])  
#         f_set.add(u_list[i][j])
# print(f_set)



# # ***************************** Problem - 4 *****************************      #not solved properly
# # Write a Python program to create and display all combinations of letters, selecting each letter from a different key in a dictionary.
# # Sample data : {'1':['a','b'], '2':['c','d']}
# # Expected Output:
# # ac
# # ad
# # bc
# # bd
# d1={'1':['a','b'], '2':['c','d']}
# l1=[]
# for i in d1.values():
#     l1.append(i)
# print(l1)  
# for i in range(len(l1)):                # i=0
#     for x,y in l1[i],l1[i+1]:
#         print(x,y)


# # ***************************** Problem - 5 *****************************   # not solved properly 
# # Nested dictionary:[{'S001': {'Adina Park': 85}}, {'S002': {'Leyton Marsh': 98}}, 
# # {'S003': {'Duncan Boyle': 89}}, {'S004': {'Saim Richards': 92}}]

# l1=['S001', 'S002', 'S003', 'S004']
# l2=['Adina Park', 'Leyton Marsh', 'Duncan Boyle', 'Saim Richards']
# l3=[85, 98, 89, 92]
# l4=list()
# d2={}

# for i,j,k in zip(l1,l2,l3):
#     d1={i:{j:k}}
#     #print(d1)
#     l4.append(d1)
# print(l4)           
    
# for i,j,k in zip(l1,l2,l3):
#     #print(i,j,k)
#     d1=dict()
#     d1[j]=k
#     d2[i]=d1
# print([d2])



# ***************************** Problem - 6 ***************************** 
import random
print('\nHello!!! Welcome to WORD GAME')
with open("list_of_words.txt",'r') as file1:
    j=file1.read().split("\n")
    # print(j)
word=random.choice(j).lower()
print(word)
life=len(word)
print(f"You have {life} chances for this unknown word")
for i in range(life):
    print('_',end=' ')
print('\n')
g1=str()
while(life>0):
    guess=str(input('\nEnter a guessing character or word : ')).lower()
    if(guess not in word):
        life -=1
        print(f'You r WRONG and {life} chances is left')
    if(life==0):
        print('\nSORRY :( u LOSE')
        print(f'The Word is {word}')
        break
    wrong=0
    g1=g1+guess
    for i in word:
        if(i in g1):
            print(i,end=' ')
        else:
            print('_',end=' ')
            wrong +=1
    if(wrong==0):
        print('\nUUURRRREEEE!!!!!!!   YOU   WON')
        break
