#Write a function “perfect()” that determines if parameter number is a perfect number. Use this function in a program that determines and prints all the perfect numbers between 1 and 1000.
#[An integer number is said to be “perfect number” if its factors, including 1(but not the number itself), sum to the number. E.g., 6 is a perfect number because 6=1+2+3].
def perfect(a):
    l=[]
    for i in range(1,a):
        if (a%i==0):
            print(i)
            l.append(i)
    if sum(l)==a:
        print(a,'number is perfect ')
        l.append(a)
    else:
        print(a," is not perfect")
    print('list of l are',l)



perfect(6)
perfect(15)


print('all numbers between 1 to 1000')
for i in range(1,1000):
    perfect(i)
    