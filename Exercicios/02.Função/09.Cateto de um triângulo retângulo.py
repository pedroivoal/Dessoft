from math import sqrt

def encontra_cateto(c1, h):

    c2 = sqrt(h**2 - c1**2)
    
    return c2

# PARA TESTAR FUNÇÃO
# print(encontra_cateto(3, 5))
