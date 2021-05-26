def get_speed(dis,time):
    speed=dis/time
    print(f'the speed is {speed}')
get_speed(1000,23)

##################################################
distance=2000
time=100
get_speed(distance,time)

###################################################
get_speed(dis=230,time=34)


##################################################
def pythagoras(per:int,base:int):
    hyp=(per**2+base**2)**0.5
    print(f'p={per},b={base}>>h={hyp}')
pythagoras(3,4)