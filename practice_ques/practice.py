#wap to create a list of 50 prime numbers
prime=[]
start=int(input('enter first number:'))
end=int(input('enter end number:'))
for num in range(start,end+1):
    count=0
    for a in range(2,num):
        if num%a==0:
            count=1
            break
    if count==0:
        prime.append(num)
print(prime)
print(len(prime))

