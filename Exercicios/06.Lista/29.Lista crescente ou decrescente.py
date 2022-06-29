def crescente(lista):

    i = 0
    while i < len(lista)-1:

        if lista[i] > lista[i+1]:
            return False
        i += 1
    return True

def decrescente(lista):

    i = 0
    while i < len(lista)-1:

        if lista[i] < lista[i+1]:
            return False
        i += 1
    return True



def classifica_lista(lista):

    if len(lista) < 2:
        return 'nenhum'
    elif crescente(lista):
        return 'crescente'
    elif decrescente(lista):
        return 'decrescente'
    else:
        return 'nenhum'
