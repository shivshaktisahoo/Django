class Person:
    def __init__(self,fname,lname,age):
        self.fname = fname
        self.lname = lname
        self.age = age
  
    def detail(self):
      print(f"{self.fname} {self.lname} has age {self.age}")  

    def __str__(self):
      return (f"{self.fname} {self.lname} has age {self.age}")  

    def __add__(self,x):  
      return self.age + x.age                             # here instead of '+'  we can use '-' # as per our choice 

    def __lt__(self,x):
      return self.age < x.age
    
    def __gt__(self,x):
        return self.age > x.age
    
    # def __div__(self,x):                            # __div__ will not work as there r two types
    #     return self.age / x.age                     # so use __truediv__  (for / divison)
                                                      # __floordiv__    (for // division)      
    def __truediv__(self,x):
        return self.age / x.age
    
    def __floordiv__(self,x):
        return self.age // x.age

    def __mul__(self,x):
        return self.age * x.age
    
    #__le__,__eq__,__ne__,__ge__    
    #__sub__,__mul__,__pow__

    def __getattr__(self, name):
        return f"No attribute as {name}"




x = Person("ABC",'DEF',43)
y = Person("shiv",'kumar',57)
z = x + y
print(z)
z=x*y
print(z)
z=x/y
print(z)
z=x//y
print(z)
print(x < y)
print(x>y)
print(x.face)     # try without __getattr__ gives a error, AttributeError: 'Person' object has no attribute 'face'
print(x.face)

d1={'detail': {101: {'Name': 'Rohit', 'Balance': 20000}, 102: {'Name': 'Shiv', 'Balance': 24000}, 103: {'Name': 'Deepesh', 'Balance': 991000}}, 'auth': {101: '101', 102: '102', 103: '103'}}
print(d1)
# max fuction
print(max(d1['detail'].keys()))            #gives biggest value