def interseccao_chaves(dic1, dic2):

    l_intecessao_de_chaves = []

    for key1 in dic1:

        if key1 in dic2:
            l_intecessao_de_chaves.append(key1)

    return l_intecessao_de_chaves
