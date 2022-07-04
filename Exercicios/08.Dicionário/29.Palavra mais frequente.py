def mais_frequente(L0):

    L_unica = []
    for palavra in L0:
        if palavra not in L_unica:
            L_unica.append(palavra)

    L_recorencia = []
    for palavra in L_unica:
        L_recorencia.append(L0.count(palavra))

    ret = L_unica[L_recorencia.index(max(L_recorencia))]

    return ret

l = ['abobora', 'chuchu', 'abobora', 'abobora', 'chuchu', 'chuchu', 'chuchu']
print(mais_frequente(l))
