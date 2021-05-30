# # ************** Problem-2 ************************* # solved

# def string_pattern(n):
#     list1 = [input(f'Enter string {i+1} :') for i in range(n)]              # List Comprehension
#     s=list(set(list1[0]))                    
#     count=0                             
#     for i in s:                         # i = r        
#         k = 1
#         for j in range(n-1):           # j = 0,1,2  & n = 4-1 = 3,
#             if i in list1[k]:           # i = r ,list1[1]=  # no, 
#                 k +=1                   # k=2,3,4
#                 if k==n:
#                     count +=1
#             else:
#                 break      
#     print(count)  
             
# string_pattern((int(input('Enter no. of terms for strings:'))))


x = ')))(()'
dummy = list(x)
remove_list = []
for index,i in enumerate(dummy):
  if i == '(':
    for j in range(index,len(dummy)):
      if dummy[j] == ')':
        remove_list.append(index)
        remove_list.append(j)
print(len(dummy)- len(set(remove_list)))