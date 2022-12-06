from math import *

def calcula_distancia_do_projetil(v,θr,y):

    t1 = v**2/19.6
    t2 = 19.6*y
    t3 = v**2 * sin(θr)**2
    dist = t1*(1 + sqrt(1 + t2/t3))*sin(2*θr)

    return dist
