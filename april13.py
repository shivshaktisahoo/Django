def cube(n):  
    print({ i:i**3 for i in range(1,n+1)})                  # dictionary comprehension ,lsit comprehension

def nested_list():
    print([[i for i in range(1,4)] for j in range(4)])    # nested list comprehension

cube(int(input('Enter no. of terms :')))
nested_list()