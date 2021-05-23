tup=(1,2,3,45,5)
print(tup)
print(type(tup))
tup1=12,23,24,45
print(tup1)
print(type(tup1))

a=[1,23,45]
a1=tuple(a)   #list to tuple
print(a1)

name='divya'
name1=tuple(name)  #string to tuple
print(name1)

a=1
b=2
c=4
d=a,b,c
print(d)

#function
a=(1,2,3,4,5,6,7,9,1,23,2,2)
print('counting all 3s= ',a.count(3))
print('index of 23 =',a.index(23))