from math import *

def reflexao_total_interna(n1, n2, θ):

    sinl = n1/n2
    sina = sin(radians(θ))
    
    if sina > sinl:
        return True
    else:
        return False
