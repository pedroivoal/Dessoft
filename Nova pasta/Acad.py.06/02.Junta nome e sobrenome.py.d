def junta_nome_sobrenome(lista1, lista2):
    i = 0
    while i  < len(lista1):
        i += 1
        lista1[i] = lista1[i]+' '+lista2[i]
    return lista1

# havia uma forma de descobrir o número de elementos
# da lista1 e criar uma lista_nome baseado nisso