x=[1,2,3,4,5,6,78,9,12,876]
#normal
x3=[]
for i in x:
    if i%3==0:
        x3.append(i)
print(x3)
#filter with lambda

m3=lambda i: i%3==0
output=list(filter(m3,x))
print(x)
print(output)
