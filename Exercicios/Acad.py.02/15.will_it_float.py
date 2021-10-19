import math

def will_it_float(P, R, r):
    V = 2 * math.pi**2 * R * r**2
    D = P*1000/V
    if D <= 0.997:
        b = True
    else:
        b = False
    return b