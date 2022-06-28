def estritamente_crescente(lista0):

    if lista0 == []:
        return []

    lista = [lista0[0]]
    i = 0
    while i < len(lista0)-1:
        if lista0[i+1] > lista[-1]:
            lista.append(lista0[i+1])
        i += 1

    return lista

# print(estritamente_crescente([1, 3, 2, 3, 4, 6, 5]))