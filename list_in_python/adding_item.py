a=[]
b=[1,12,13,14]
                    #add single value to a list
a.append('divya')
print(a)
b.append(15)
print(b)
                    #insert single item in a list
c=[1,2,3,4,5]
c.insert(1,12)
print(c)
d=['divya','riya','ayushi']
d.insert(2,'gita')  #insert gita at idx 2 and everything shift to right
print(d)
                    #replace a value at an index
a[0]=100
print(a)
b[-1]='gita'
print(b)
                    #join a list to existing list
a.extend([34,36,38])
print(a)
b.extend(a)
print(b)