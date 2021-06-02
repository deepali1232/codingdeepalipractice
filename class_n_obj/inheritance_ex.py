class Animal:
    is_alive=True
    def eat_food(self,food):
        print('animal eats',food)



class Vertebrates(Animal):
    has_spine=True

class Bird(Vertebrates):
    has_wings=True
    def fly(self):
        print('bird is flying')

a=Animal()
a.eat_food('plant')
a.eat_food('fish')
print('living',a.is_alive)

b=Vertebrates()
b.eat_food('plant')
b.eat_food('meat')
print('living',b.is_alive)
print('apines',b.has_spine)

c=Bird()
c.eat_food('worms')
c.fly()
c.eat_food('worms')
c.fly()
print('spine',c.has_spine)
print('wings',c.has_wings)
print('alive',c.is_alive)