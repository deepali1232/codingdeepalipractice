#function,#update,#pop,#pop items,#get,#keys,#values,#items,#clear

fruits={'apple':100,'banana':40,
'cherry':130,'dragonfruit':200}

print('update values in dict')
new_fruit={'guava':35,'peach':43}
fruits.update(new_fruit)
print(fruits)

#remove value from dict
fruits.pop('cherry')
print(fruits)

#find item bettr version

if 'orange' in fruits:
    fruits.pop('orange')
    print(fruits)
else:
    print('orange  not found')

last_item=fruits.popitem()
print(fruits)

print(f'{last_item} removed from fruits') #f stands for format

#accessing value from dict
print(fruits['apple'])

#through get
print(fruits.get('apple'))
print(fruits.get('grapes','price not found'))


#accessing keys,values
print(fruits.keys())
print(list(fruits.values()))  #convert into list
print(fruits.items())

#looping in dict
print('normal loop get only values')

for i in fruits:
    print(i)

print('get only values')
for i in fruits.values():
    print(i)

print('get both values')
for k,v in fruits.items():
    print(k,'--->',v)

#only values
for i in fruits:
    print(fruits[i])
    