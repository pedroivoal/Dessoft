def inverte_lista(lista0):

    lista = []

    i = 1
    while -i >= -len(lista0):
        lista.append(lista0[-i])
        i += 1

    return lista


print(inverte_lista([1, 3, 2, 3, 4, 6, 5]))