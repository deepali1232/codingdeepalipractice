# sum of digit

number  = int(input('enter a digit'))
total = 0
while number>0:
    r = number % 10         # get the last digit
    total += r              # add the digit to total
    number = number // 10   # remove the last digit from number

print('total',total)