import math

def calcula_distancia_do_projetil(v,θr,y):
    #θr = math.radians(θc)
    t1 = v**2/19.6
    t2 = 19.6*y
    t3 = v**2 * math.sin(θr)**2
    dist = t1*(1 + math.sqrt(1 + t2/t3))*math.sin(2*θr)
    return dist

