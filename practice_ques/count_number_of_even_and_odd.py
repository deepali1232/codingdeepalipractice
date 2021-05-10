even=0
odd=0
for i in range(1,200):
    if i%2==0:
        even+=1
    else:
        odd+=1
print("total evens",even)
print("total odds",odd)