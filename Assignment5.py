# ************************* Problem-1 ******************         #solved
# Write a Python script to concatenate following dictionaries to create a new one.
# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
dic4={}                                     # creates a new dictionary    
for i in dic1.items():                    
    print(i)
#     dic4[i]=j                              # dic1 items goes into dic4
# for i,j in dic2.items():
#     dic4[i]=j                               # dic2 items goes into dic4
# for i,j in dic3.items():
#     dic4[i]=j                               # dic3 items goes into dic4
# print(dic4)

# # ************************* Problem-2 ******************         #solved
# # Write a Python program to match key values in two dictionaries.
# # Sample dictionary: {'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2}
# # Expected output: key1: 1 is present in both x and y

# dic1={'key1': 1, 'key2': 3, 'key3': 2}
# dic2={'key1': 1, 'key2': 2}
# for i in dic1.items():
#     for j in dic2.items():
#         if(i==j):
#             print(i,'item is present in both dictionary')



# # ************************* Problem-3 ******************         #solved
# # Check a number/string is palindrome or not

# chr=str(input('Enter a Number or a string : ')).lower()
# #print(chr)
# #print(chr[::-1])
# if(chr==chr[::-1]):
#     print(f'{chr} is a palindrome')
# else:
#     print(f'{chr} is not a palindrome')