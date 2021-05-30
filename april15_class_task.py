# #**************** Problem -3 ***************      # solved
def logic(n,list1):
    for i in list1:
        if "0" in i:
            return 'okay'
            break
    
n = int(input('enter no. of elements:'))
list1 = [(input(f'Enter number {i+1} :')) for i in range(n)]
print(logic(n,list1))

# **************** Problem -4 ***************        # solved
def Encrypt(str1):
    list1 = str1[::-1].split(" ")[::-1]
    str2=''
    for i in range(len(list1)):
        str2 += (list1[i]+'arg')
    return str2

def Decrypt(encry):
    str2=''
    list1 = encry[::-1].split('gra')[::-1]
    list1.pop()
    for i in range(len(list1)):
        str2 += (list1[i]+' ')
    return str2

str1=input("Enter string:")
encry = Encrypt(str1)
print("Encryption is : ",encry)
print("Decryption is : ",Decrypt(encry))

