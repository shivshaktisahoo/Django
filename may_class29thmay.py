# import random
# with open('test_29thmay.txt', 'w') as file1:
#     for i in range(10):
#         file1.write(str(random.randrange(1, 100))+',')
# with open('test_29thmay.txt', 'r') as file1:
#     y = file1.readlines()
# print(y,type(y))
# list1 = y[0].split(',')
# print(list1)
# sum1 = 0
# for i in list1:
#     if len(i)>0:
#         sum1 +=int(i)
# print(f"Sum is {sum1}")   
# with open('test_29thmay.txt', 'a') as file1:
#     file1.write("Sum is "+str(sum1))

# Dictionary problem
# {"English":98,'Social':67,'Science':78}
# import ast
# with open('test_29thmay.txt', 'r') as file1:
#     y = file1.read()
#     y = ast.literal_eval(y)
# # print(y,type(y))
# total = y['English']+y['Social']+y['Science']
# percen = total/3
# # print(total,percen)
# y['Total'] = total
# y['Percentage'] = percen
# # print(y)

# with open('test_29thmay.txt', 'w') as file1:
#     file1.write(str(y))