#with basic logic
x=[12,12,34,47,89,28]
x2=[]                       #blank list
for i in x:                 #loop
    sqr=i**2                #sqr of each value
    x2.append(sqr)          #stored in x2
print(x)
print(x2)

#can be done with comprehension with one line
#new list=[operation loop]
x=[1,2,3,4]
print(x)
x2=[i**2 for i in x]
print(x2)