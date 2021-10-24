#
def monta_dicionario(listaK, listaV):

    dic = {}
    c = 0

    for i in listaK:
        dic[i] = listaV[c]
        c += 1
    
    return dic