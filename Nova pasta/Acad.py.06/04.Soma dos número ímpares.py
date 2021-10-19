def soma_impares(lista):
    i = 0
    s = 0
    while i < len(lista):
        if lista[i]%2 == 1:
            s += lista[i]
        i += 1
    return s