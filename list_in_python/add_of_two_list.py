# add each item from 2 list and store result in 3rd list

x = [41,92,93,33,42,73,56,61,27]
y = [23,22,13,23,43,52,36,7]
z = []
for i,j in zip(x,y):
    z.append(i + j)
print(x)
print(y)
print(z)
