from math import sqrt, pi, e

def calcula_gaussiana(x, mi, sig):

    ex = -0.5*((x-mi)/sig)**2
    f = e**ex/(sig*sqrt(2*pi))

    return f
