a=[1,2,3,4,5,6]
odd_sqr=[]
for i in a:
    if i%2!=0:
        odd_sqr.append(i**2)
print(a)
print(odd_sqr)


even_sqr=[i**2 for i in a if i%2==0]
print(even_sqr)