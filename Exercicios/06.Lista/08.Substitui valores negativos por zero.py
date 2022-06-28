def zera_negativos(lista):

    lista_z = []

    for i in lista:

        if i < 0:
            lista_z.append(0)
        else:
            lista_z.append(i)

    return lista_z