# ************************* Problem 1: *************************        # solved
# 1: Write a Python program to reverse the digits of an integer.
# Input : 234
# Input : -234
# Output: 432
# Output : -432

reverse_number = lambda n : -1*int(str(abs(n))[::-1]) if n<0 else int(str(n)[::-1])
print(reverse_number(234))
print(reverse_number(-234))

# ************************* Problem 2: *************************        # solved
# 2: Write a Python program to check a sequence of numbers is an arithmetic progression or not.
# Input : [5, 7, 9, 11]
# Output : True
# In mathematics, an arithmetic progression or arithmetic sequence is a sequence of
# numbers such that the difference between the consecutive terms is constant.
# For example, the sequence 5, 7, 9, 11, 13, 15 ... is an arithmetic progression with
# common difference of 2.

def ap_check(list1):
    first_val = list1[0]
    diff = list1[1] - list1[0]
    l2 = []
    l2.append(first_val)
    for i in range(2,len(list1)+1):
        val = first_val + (i-1)*diff        # Formula for A.P : 
        l2.append(val)
    if l2==list1:
        return True
    return False
list1 = [5, 7, 9, 11, 13]           # must return True, as it is A.P
list2 = [1, 2, 4, 5, 6, 8, 20]      # must return False, as it is not A.P
print(ap_check(list1))
print(ap_check(list2))


# ************************* Problem 3: *************************        # solved
# 3: Write a Python program to compute the sum of the two reversed numbers and display the sum in reversed form.
# Input : 13, 14
# Output : 27
# Note : The result will not be unique for every number for example 31 is a reversed form of 
# several numbers of 13, 130, 1300 etc. Therefore all the leading zeros will be omitted.

rev_sum = lambda n1,n2 : int(str(int(str(n1)[::-1]) + int(str(n2)[::-1]))[::-1])
print(rev_sum(13,14))
print(rev_sum(1400,12))     # 1400-> 41 and 12->21, 41+21=62-> 26
print(rev_sum(50,500))      # 50-> 5 and 500->5, 5+5=10-> 1

# ************************* Problem 4: *************************        # solved
# 4: Create file and write 10 trails for question no 3 in that file
# in file write:
# example: {‘elements’: [13, 14],‘sum’:27} plus other……

str1 = '''
Input : 13, 14
Output : 27

Input : 1400, 12
Output : 26

Input : 50, 500
Output : 1
'''
rev_sum1 = lambda l1 : int(str(int(str(l1[0])[::-1]) + int(str(l1[1])[::-1]))[::-1])   
with open("test_28thmay.txt","w") as file1:
    for i in range(10):
        x = [int(input("Enter the numbers:")) for i in range(2)]
        y = rev_sum1(x)
        dict1 = {"Elements ": x , "reverse_sum" : y}
        file1.write(str(dict1)+"\n")

# ************************* Problem 5: *************************        # solved
# 5: Open that created file and display trails and result of that trails
# Input : 13, 14
# Output : 27
# plus other results in same file
with open("test_28thmay.txt",'r') as file2:
    print(file2.read())                 # displaying trails and results

# ************************* Problem 6: *************************        # solved
# 6: Try appendoperation with mode ‘a’, operations are same write, writelines.
with open("test_28thmay.txt",'a') as file3:
    file3.write("I am appending now again for above blocks")
    for i in range(10):
        x = [int(input("Enter the numbers:")) for i in range(2)]
        y = rev_sum1(x)
        dict1 = {"Elements ": x , "reverse_sum" : y}
        file3.writelines(str(dict1)+'\n')
     