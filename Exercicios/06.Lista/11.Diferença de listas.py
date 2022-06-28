
def subtracao_de_listas(l_1, l_2):

    diferenca = []

    for i in l_1:
        if i not in l_2:
            diferenca.append(i)

    return diferenca
