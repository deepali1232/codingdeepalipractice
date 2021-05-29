def mean(*numbers):
    if numbers:
        
        print("mean>>>",sum(numbers)/len(numbers))
    print(numbers)

mean()
mean(1)
mean(12,2,34,5,6,89)
                                                          #any number of value use *


def agg(*numbers,operation='sum'):
    if numbers:
        if operation=='sum':
            print('total',sum(numbers))
        elif operation=='mean':
            print('mean',sum(numbers/len(numbers)))
        elif operation =='max':
            print('max',max(numbers))
agg(12,23,34,44)
agg(65,87,34,84,36,56,74,86,operation='sum')
agg(45,78,2,34,43,54,43,43,operation='max')
agg(42,97,27,21,29)


def setting(**info):  #every name and value**
    for k,v in info.items():
        print(k,v,end='')
setting(color='red',x=28,y=39,size=(100,100))
setting(font="calibri",fontsize=20)