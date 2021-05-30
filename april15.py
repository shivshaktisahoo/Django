# x = '()()'
# # ( )

# list_x = list(x)
# dummy = list_x
# for index, value in enumerate(list_x):#index = 0,a=1 dummy = ['(',')']
#     print('line7')
#     print(index,value)
#     if value == '(':
#       a = dummy.index(')')
#       print(index,a)
#       if index < a: #0<1
#         dummy.pop(index)
#         dummy.pop(a-1)
#         print('line12')
#     if value == '{':
#       a = dummy.index('}')
#       if index < a:
#         dummy.pop(index)
#         dummy.pop(a-1)  
#     print('line19')
# print(dummy)




# x = '()()'
# list_x = list(x)
# dummy = list_x

# for index, value in enumerate(list_x):
#     if value =='(': 
#       for i in range(index,len(list_x)-1):
#         print(index)  
#         # if list_x[i] == ')':
#         #   b = dummy.index('(')
#         #   dummy.pop(b)
#         #   a = dummy.index(')')
#         #   dummy.pop(a)
# print(dummy)

#**************** Problem -3 ***************
def logic(n,list1):
    for i in list1:
        if "0" in i:
            return 'okay'
            break
    
n = int(input('enter no. of elements:'))
list1 = [(input(f'Enter number {i+1} :')) for i in range(n)]
print(logic(n,list1))

# **************** Problem -4 ***************
def logic1(str1):
    list1 = str1[::-1].split(" ")[::-1]
    print(list1)
    for i in range(len(list1)):
        print(list1[i],end='')
        print('arg',end='')
    return ""


str1=input("enter string:")
print(logic1(str1))

    