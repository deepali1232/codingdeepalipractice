vowels=('a','e','i','o','u')
count=0
string='i am girl.'
for s in string:
    if s in vowels:
        count+=1
print(count)