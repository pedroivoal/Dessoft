
def pacotes_correio(remessa):

    ordem = []
    tamanhos = []
    numero = []

    for i in remessa:
        tamanhos.append(i[2])
        numero.append(i[0])
        ordem.append(i[1])

    t_min = min(tamanhos)
    t_max = max(tamanhos)
    if t_max != t_min:
        return 'tamanho errado'
    
    n = len(remessa)
    n_min = min(numero)
    n_max = max(numero)
    if n_max != n_min or n_max!=n:
        return 'pacote perdido'

    ordinal = []
    i = 1
    while i <= len(remessa):
        ordinal.append(i)
        i += 1

    if ordem != ordinal:
        return 'ordem errada'
    
    return 'tudo certo'

# print(pacotes_correio(remessa = [[4,1,20],[4,2,20],[4,3,20],[4,4,20]]))