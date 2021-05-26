#no argument fun

def hello():
    '''this is a very important function'''             #documentation strings
    print('hello frnds')
hello()
hello()
hello()


for i in range(10):
    hello()

def world():
    print('this is nice function')
    hello()
    print('it is good')
world()

def divide():
    '''take input'''
    x=int(input('enter number>>>'))
    y=int(input('enter another number>>>'))
    print(x/y)
divide()

