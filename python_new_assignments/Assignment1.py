
# # *********************** Problem - 1 ****************************           # solved
# # Write a Python program which accepts the radius of a circle from the user and compute the area.
# # Sample Output :
# # r = 1.1
# # Area = 3.8013271108436504

# r = float(input("Enter a Radius of a Circle = "))
# print(f"Area of Cirlce is {(22/7)*r*r} unit")



# # *********************** Problem - 2 ****************************           # solved
# # Write a Python program to sum of two given integers. However, if two values are equal sum will be zero.

# print('Enter 2 integers:')
# x,y = int(input("x : ")),int(input("y : "))
# if x==y:
#     print('Sum is 0')
# else:
#     sum = x+y
#     print(f'sum is {sum}')


# # *********************** Problem - 3     ****************************        #  solved
# # Write a Python program to test whether a number is within 100 of 1000 or 2000.
# # I.e what ever input given by user, gap between that number and 1000 must be with in 100 or gap
# # between that number and 2000 must be with in 100

# n = float(input("Enter the Number : "))
# a = abs(2000-n)
# b = abs(1000-n)
# if(a<=100) or (b<=100):
#     print("in between 100")
# else:
#     print("outside 100")



# # *********************** Problem - 4 ****************************           # solved
# # Write a Python program that will accept the base and height of a triangle and compute the area.


# b = float(input("Enter base of a triangle: "))
# h = float(input("Enter height of a triangle: "))
# print(f'Area of Triangle is {(1/2)*b*h} unit')





# # # *********************** Problem - 5 ****************************          # solved
# # # Ask subject marks from user and 
# # # display him total, percentage, grade ( pass,1st Division, 2nd Division or Distinction)
# name = input("Enter your Name:")
# m = float(input("Enter Maths mark:"))
# s = float(input("Enter Science mark:"))
# sc = float(input("Enter Socialscience mark:"))
# h = float(input("Enter Hindi mark:"))
# p = ((m+s+sc+h)/400.0)*100 
# print(f"Name: {name} \t Your Total marks is {m+s+sc+h} \t Percentage is {p} \t Grade is ",end="")
# if p<=100.0 and p>=80.0:
#     print('"Distinction"')
# elif p<80.0 and p>=60.0:    
#     print('"1st division"')
# elif p<60.0 and p>=40.0:
#     print('"2nd division"')
# elif p<40.0 and p>=30.0:
#     print('"3rd division"')
# else:
#     print('"FAIL"')   
  
# print("\n")
# print("\\n")
# print("\t")
# print("/'\t")
# print("ha\npp\ty")
# print(r"ha\npp\ty")     # o/p- ha\npp\ty 

# sum = 0
# x = "shiv"
# for i in x:
#     m = int(input("enter ur marks: "))
#     sum +=m
# print(sum)

# def average_finder(*args):
#     average = []
#     print(*args)
#     for pair in zip(*args):    # in this *args unpack is doing and pair is (1,4,7) , (2,5,8), (3,6,9) an so on 
#         print(pair)
#         average.append(sum(pair)/len(pair))
#     return average


# print(average_finder([1,2,3],[4,5,6],[7,8,9]))


# x = "shivarx"
# print(x[:3:-1])



# n = int(input("number:"))
# sum = 0
# for i in range(n):
#     mrk = int(input(f"enter mark {i+1}:"))
#     sum +=mrk
# print(f"Total mark is {sum}")

# sum1 = 0
# list1 = [i for i in range(1,11)]
# # for i in list1:
# #   sum1 +=i
# # print(f"Sum is {sum1}")
# print(sum(list1))


# a = [1,3,5,7]
# b = [2,4,6,8]
# cartesian_product = [(i,j) for i in a for j in b]
# print(cartesian_product)


x = {
    "Name":"Vishal",
     "Age": 32,
     "Salary":300000,
     "Education":{"Maths":56,"Science":87,'Hindi':65, "Social":78}
}
x["Education"]["Total"] = sum(x["Education"].values())
x["Education"]["Percentage"] = (x["Education"]["Total"]/400)*100
print(x)