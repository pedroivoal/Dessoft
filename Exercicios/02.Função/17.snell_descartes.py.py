from math import sin, radians, asin, degrees

def snell_descartes(n1, n2, θ1):

    k = n1/n2
    θ2 = k * sin(radians(θ1))
    
    r = asin(θ2)
    r1 = degrees(r)
    
    return r1