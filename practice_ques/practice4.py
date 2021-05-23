#wap to store all the armstrong number till 100000
for i in range(100001):
    num=i
    result=0
    n=len(str(i))
    while(i!=0):
        digit=i%10
        result=result+digit**n
        i=i//10
    if num==result:
        print(num)

#or another methhod
for num in range(1,100000):
    pow=len(str(num))
    temp=num
    total=0
    while num > 0:
     digit  = num % 10
     total+=digit**pow
     num=num//10
     if temp==total:
        print(temp,end=',')