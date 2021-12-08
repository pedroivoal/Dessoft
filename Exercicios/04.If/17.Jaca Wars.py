# 
from math import radians, sin

def distance(speed,c_degrees):

    r_degrees = radians(c_degrees)

    dist = speed**2 *sin(2*r_degrees)/9.8

    return dist

speed = float(input())
c_degrees = float(input())

dist = distance(speed, c_degrees)

if dist < 98:
    print('Muito perto')
elif dist > 102:
    print('Muito longe')
else:
    print('Acertou!')