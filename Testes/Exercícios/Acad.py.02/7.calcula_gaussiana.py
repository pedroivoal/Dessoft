import math

def calcula_gaussiana(x, mi, sig):
    ex = -0.5*((x-mi)/sig)**2
    f = math.e**ex/(sig*math.sqrt(2*math.pi))
    return f