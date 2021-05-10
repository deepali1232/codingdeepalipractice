string='i am happy girl and u are sad person.'
vowels=('a','e','i','o','u')
for x in string.lower():
    if x in vowels:
        string=string.replace(x,' ')
print(string)