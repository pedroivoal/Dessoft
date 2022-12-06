from math import radians, tan

def area_pentagono(l):

    ang = radians(54)
    area = 2.5 * l * l * tan(ang) / 2

    return area

# PARA TESTAR FUNÇÃO
# print(area_pentagono(2))
