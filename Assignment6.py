# *************************** Problem - 1 **************************            #solved
# Strong number
# Strong number is a special number whose sum of the factorial of digits is equal to the original number. 
# For Example: 145 is strong number. Since, 1! + 4! + 5!
def factorial(x):
    mul=1
    for i in range(1,x+1):                      # range from 1 - 6 (if no. is 5) 
        mul *=i                                 # multiply i with mul (1*1=1, 1*2=2, 2*3=6, 6*4=24,.....)
    return mul                                  # return 120

def extract(x):
    sum=0
    n1 = x                                      # no is 145
    while(x!=0):
        n = x % 10                              # n = 145 % 10 = 5
        f = factorial(n)                        # f = 120 calls factorial function
        x = x // 10                             # x = 14
        sum += f                                # adding fact. value with sum
    if(sum==n1):
        print(n1," is a Strong number")
    else:
        print(n1," is not a Strong number")


while(True):
    try:
        n = int(input("Enter a number : "))          # If user enters wrong input, try & exception is used to handle Error        
        break
    except:
        print('Try to input number only')
extract(n)                                           # Calling extract function with passing parameter 'n'


# *************************** Problem - 2 **************************
# Write a Python function to check whether a string is a pangram or not.
# Note : Pangrams are words or sentences containing every letter of the alphabet at least once.
# For example : "The quick brown fox jumps over the lazy dog"

def pangram(s):
    s1={'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}
    org_str=s
    s=s.lower()                                         # converted to lower string
    s3=set()                                                
    for i in s:
        if i in s1:
            s3.add(i)                                   # Adding correct values of i in s3 set
    if(s3==s1):
        print(f"\"{org_str}\" is a pangram sentence")
       
    else:
        print(f"\"{org_str}\" is not a pangram sentence")

s2="My girl wove six dozen plaid jackets before she quit"      # Input given
pangram(s2)                                                    # Calling perfect function with passing parameter s2       



# *************************** Problem - 3 **************************         #solved
# Write a Python function to check whether a number is perfect or not.
def perfect(x):
    sum=0
    for i in range(1,x):
        if(x%i==0):
            sum +=i
    if(sum==x):
        print(x, "is a perfect number" )
    else:
        print(x, "is not a perfect number" )

while(True):
    try:
        n = int(input("Enter a number : "))          # If user enters wrong input, try & exception is used to handle Error        
        break
    except:
        print('Try to input number only')
perfect(n)                                           # calling perfect function with passing parameter 'n'






