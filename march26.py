x="shivshakti"
print(x[::-1])
x=[1,2,3,'shiv','rohit',[1,2,3,4,[1,24,56]]]
x.append(["happy"])
print(x)
x.insert(2,99)
print(x)
x.insert(2,"python")
print(x)

y=["happy","sad","angry"]
y.remove('sad')
print(y)

x.pop()
print(x)

x.pop(1)
print(x)

for i in x:
    print(i)

for i in range(len(x)):
    print(x[i])
y=["4","1","2","5"]
y.sort()
print(y)


a=(1,2,3,"shiv",(23,56),[12,67,90])
print(a)
# a.append("d")                 # AttributeError: 'tuple' object has no attribute 'append'
a=list(a)                       # converting to a list, perform append & then convert to a tuple
a.append("d")
print(a)
a=tuple(a)
print(a)



