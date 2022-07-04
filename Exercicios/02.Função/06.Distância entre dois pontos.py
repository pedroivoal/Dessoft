from math import sqrt

def distancia_euclidiana(x1, y1, x2, y2):

    d = sqrt((x1-x2)**2 + (y1-y2)**2)
    
    return d

# PARA TESTAR FUNÇÃO
# print(distancia_euclidiana(0, 0, 3, 4))
