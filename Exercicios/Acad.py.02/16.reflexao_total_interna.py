import math

def reflexao_total_interna(n1, n2, θ):
    sinl = n1/n2
    sina = math.sin(math.radians(θ))
    if sina > sinl:
        r = True
    else:
        r = False
    return r
