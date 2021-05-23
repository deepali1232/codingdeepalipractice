#cricketer names
cricketer=[]
while True:
    name=input('enter names:')
    if not name:
        break
    elif name[0].isupper():
        cricketer.append(name)
print(cricketer)


