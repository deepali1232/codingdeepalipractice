class Person:

    def __init__(self,name,age,gender):
        self.name=name
        self.age=age
        self.gender=gender

    def work(self):
        print('the person is working')

    def eat(self):
        print(f'the{self.name}is eating')

    def purchase(self,name):
        print(f'the {self.name}is sleeping')
    
class Student(Person):
    def __init__(self,name,age,gender,college,cls):
        super().__init__(name,age,gender)
        self.college=college
        self.cls=cls 

    def study(self):
        print(f'{self.name}is studying')

    def work(self):
        print(f'{self.name} is working on a project')

    def purchase(self,item):
        super().purchase(item)
        print('with the help of tution money.')

if __name__=='__main__':
    p=Person('divya',20,'male')
    p.work()
    p.purchase('mobile')

    s=Student('raghav',12,'male','DMSRS','7TH')
    s.work()
    s.purchase('book')