a={1,2,3,4,5,6,7,8}
b={1,4,7}
c={89,80,38,76,90}
d={28,38,98,19,34,87,56}

#set fun,add,remove,clear,pop,issubset,isdisjoint,isuperset
d.add('apple')
print(d)

c.remove(80)
print(c)

a.update({12,87,78}) #add values to existing set
print(a)

d.pop()
print(d)

print(a.issuperset(c),'a is superset of a')

print(b.issuperset(d)," b is superset of d")

if a.isdisjoint(d):
    print('not related')
else:
    print('a and d are related')

if b.issubset(a):
    print('b is subset of a')
else:
    print('b is not subset of a')

if c.issubset(a):
    print('true')
else:
    print('not a subset')

#set math
#union ,take every unique value
print(a.union(d))
print(a|d)  #  | IS USED FOR UNION

print(b.difference(c))
print(b - c)

print(a.intersection(d))
print(a & d)

print(a.symmetric_difference(c))
print(a^c)