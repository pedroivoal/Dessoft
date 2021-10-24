#
def organiza_filas(lis_r):
    # faixas etárias
    lis_20 = []
    lis_40 = []
    lis_60 = []
    lis_v = []

    # confere a faixa etária de cada inscrito
    for insc in lis_r:

        if insc[1] < 21:
            lis_20.append(insc[0])
        elif insc[1] < 41:
            lis_40.append(insc[0])
        elif insc[1] < 61:
            lis_60.append(insc[0])
        else:
            lis_v.append(insc[0])

    # recebe a lista de cada faixa etária
    # (facilita a criação de novas filas)
    lis_saida = [lis_20, lis_40, lis_60, lis_v]

    return lis_saida