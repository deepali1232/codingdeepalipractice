name='divya'  #outside fun
def who():
    print(f'who am i')
    print(f'i am {name}') #can be access inside fun
who()


def what():
    print('who are u')
    name='riya'
    print(f'i am {name}')
what()
print(name)#global name



def update_name():
    global name #if you want to modify name
    print('old',name)
    name='ayushi'
    print('new',name)  #updated name
update_name()
print('new',name)