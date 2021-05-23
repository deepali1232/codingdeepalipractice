x={2,3,5,33,7,'divya',90}
print(x)
y={'di','kriti'}
print(y)
z={1,2,3,4,1,2,3}
print(z)
print(type(z))
#set value cannot indexed or slice
a=[1,2,3,4,5]
a_set=set(a)  #list to set
print(a,a_set)
b=(1,2,3,4,5,7)
b_set=set(b)  #tuple to set
print(b,b_set)
#PRINT EACH ELEMENT OF SET
for i in a_set:
    print(i,end=' ')

