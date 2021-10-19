def classifica_triangulo(l1, l2, l3):

    if l1 == l2 and l2 == l3:
        tri = 'equilátero'
    elif l1 != l2 and l1 != l3 and l2 != l3:
        tri = 'escaleno'
    else:
        tri = 'isósceles'

    return tri
