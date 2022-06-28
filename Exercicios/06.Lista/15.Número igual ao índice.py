def numero_no_indice(lista0):

    lista_r = []
    i = 0
    while i < len(lista0):
        if lista0[i] == i:
            lista_r.append(i)
        i += 1
        
    return lista_r

print(numero_no_indice([1, 3, 2, 4]))