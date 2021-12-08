// 
import math

def snell_descartes(n1, n2, θ1):
    k = n1/n2
    θ2 = k * math.sin(math.radians(θ1))
    return θ2
