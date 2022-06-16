from math import *

def haversine(r, fi1, lamb1, fi2, lamb2):

    fi1 = radians(fi1)
    fi2 = radians(fi2)
    lamb1 = radians(lamb1)
    lamb2 = radians(lamb2)

    p1 = sin((fi2-fi1)/2)**2
    p2 = cos(fi1) * cos(fi2) * sin((lamb2-lamb1)/2)**2

    d = 2*r * asin(sqrt(p1 + p2))

    return d