from math import sin, radians

def snell_descartes(n1, n2, θ1):

    k = n1/n2
    θ2 = k * sin(radians(θ1))
    
    return θ2
