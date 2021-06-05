class Student:
    def __init__(self,name,age,college,cls,section,gender):
        self.name=name
        self.age=age
        self.college=college
        self.cls=cls
        self.section=section
        self.gender=gender

from dataclasses import dataclass

@dataclass
class Studentv2:
    name:str
    age:int
    college:str
    cls:str
    section:str
    gender:str

@dataclass
class Marks:
    Student:Studentv2
    total:int
if __name__=='__main__':
    s1=Student('divya',12,'akpmds','7th','b','male')
    s2=Student('rani',12,'apdfr','7th','A','female')
    s3=Studentv2('raju',16,'akp','11th','d','male')
    print(s3.name)
    print(s1.name)
    print(s2.name)
    print(s1.cls)
    print(s2.cls)
    print(s3.cls)
    print(s3)
    
    m=Marks(s3,77)
    print(m)



class Mobile:
    def __init__(self,brand,model,price):
        self.brand=brand
        self.model=model 
        self.price=price


if __name__=='__main__':
    m1=Mobile('samsung','mo2',8000)
    m2=Mobile('redmi','note 8',1000)
    print(m1.brand)
    print(m2.brand)
    print(m1.price)
    print(m2.price)




