#
#
# Q1
def formata_data(data, formato):
    
    pos_ano = formato.find('a')
    pos_mes = formato.find('m')
    pos_dia = formato.find('d')
    sep = formato[1]

    if pos_ano == 4:
        pos_ano = 2
    elif pos_ano == 2:
        pos_ano = 1
    if pos_mes == 4:
        pos_mes = 2
    elif pos_mes == 2:
        pos_mes = 1
    if pos_dia == 4:
        pos_dia = 2
    elif pos_dia == 2:
        pos_dia = 1


    data = data.split(sep)

    if len(data[pos_ano]) == 2:
        data[pos_ano] = '20' + data[pos_ano]
    if len(data[pos_mes]) == 1:
        data[pos_mes] = '0' + data[pos_mes]
    if len(data[pos_dia]) == 1:
        data[pos_dia] = '0' + data[pos_dia]
    
    form_data = data[pos_ano] + '-' + data[pos_mes] + '-' + data[pos_dia]

    return form_data

#
#
# Q2
def retorno_bovespa(di, df):

    with open('bovespa.csv', 'r') as arq:
        bovespa = arq.read()

    if di not in bovespa or df not in bovespa:
        return 'sem dados'
    else:
        bovespa_ls = bovespa.split('\n')
        for bovespa_l in bovespa_ls:
            bovespa_e = bovespa_l.split(',')
            if di == bovespa_e[0]:
                Fi = float(bovespa_e[4])
                break
        for bovespa_l in bovespa_ls:
            bovespa_e = bovespa_l.split(',')
            if df == bovespa_e[0]:
                Ff = float(bovespa_e[4])
                break

        retorno = (Ff - Fi)/Fi

        return retorno