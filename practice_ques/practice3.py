#wap to create a nested list using user input ,the length of list depend upon user
nest_list=[]
while True:
    items=input('enter values>>>').split(',')
    if len(items)>1 and items[0]!='':   
        nest_list.append(items)
    else:
        break
print(nest_list)