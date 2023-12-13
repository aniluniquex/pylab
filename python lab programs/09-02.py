import math

def ball_collide(ball_tuple1,ball_tuple2):
    d=math.sqrt((ball_tuple1[0]-ball_tuple2[0])**2 + 
                (ball_tuple1[1]-ball_tuple2[1])**2)
    if(d<=(ball_tuple1[2]+ball_tuple2[2])):
        return True
    else:
        return False

ball_tuple1=(-2,-2,3)
ball_tuple2=(1,1,3)
collision=ball_collide(ball_tuple1,ball_tuple2)
if(collision):
    print("Balls are collide.")
else:
    print("Balls are not collide.")
