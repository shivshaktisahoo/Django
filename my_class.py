class Laptop:
    def __init__(self,brand_name,model_name,price):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
        self.laptop_name = brand_name +' '+ model_name          #can be possible if no of attributrs is less in __init__s

    def percentage(self,d):
        return self.price-(self.price*(d/100))


l1 = Laptop('hp','R00015-tx',100000)                             # l1 , l2 are the objects or instances
l2 = Laptop('asus','abacd',40000)

print(l1,type(l1))
print(l1.brand_name, l1.model_name, l1.price)
print(l2.brand_name, l2.model_name, l2.price)
print(l1.laptop_name)
print(l1.percentage(40))
print(l1.__dict__)                                  # to see what are things in l1 object & returns a dictonary
#l2.discount_off = 50                                # Refer these and complete video no. 190(harshit varisth)



class Person:
    count_instance = 0                                # class variable  # for every object they has class variable 
    def __init__(self,first_name,last_name,age):
        Person.count_instance +=1                       #how to use class variable by writing in such way:  class_name.class_variable 
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    @classmethod
    def count_instances(cls):             # class method     # cls is written for class(in place of self)           
        return f"you have created {cls.count_instance} instances of {cls.__name__} class"      #{}-placeholder,  cls.__name__ is used to get class name

    def full_name(self):                  # instance method   # these function is method as they r inside a class
        return f"{self.first_name} {self.last_name}"
    
    def is_above_18(self):
        return self.age>18

p1 = Person('shiv','shakti',20)
p2 = Person('deepak','sahoo',18)
print(p1.full_name())                           #full_name() is a method here, a function created inside a Person class
#can be done in similar way
# Person.full_name(p1)
print(Person.full_name(p1))                        # class_name.method_name(object)

print(p1.is_above_18())
print(Person.count_instances())


l1 = [1,2,3]
# clear(), pop(), append()   # methods (function created inside a list class)

# l1.clear()
# print(l1)
# In a similar way we can do 
# class_name.method_name(object)
# list.clear(l1)
# print(l1)

# l1.append(10)
# print(l1)
list.append(l1,10)          # class_name.method_name(object,parameters)
print(l1)


#circle
class Circle:
    pi = 3.14                # class Variable
    def __init__(self,radius):
        #instances variable
        self.radius = radius
    
    def circumference(self):
        return 2 * Circle.pi * self.radius          # Circle.pi which is the variable of class Circle must be write in this way

c1 = Circle(4)
print(c1)
print(c1.circumference())