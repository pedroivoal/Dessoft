def formata_data(data, formato):
    
    p_ano = formato.find('a')
    p_mes = formato.find('m')
    p_dia = formato.find('d')
    sep = formato[1]

    if p_ano == 4:
        p_ano = 2
    elif p_ano == 2:
        p_ano = 1
    if p_mes == 4:
        p_mes = 2
    elif p_mes == 2:
        p_mes = 1
    if p_dia == 4:
        p_dia = 2
    elif p_dia == 2:
        p_dia = 1

    data = data.split(sep)

    if len(data[p_ano]) == 2:
        data[p_ano] = '20' + data[p_ano]
    if len(data[p_mes]) == 1:
        data[p_mes] = '0' + data[p_mes]
    if len(data[p_dia]) == 1:
        data[p_dia] = '0' + data[p_dia]
    
    form_data = data[p_ano] + '-' + data[p_mes] + '-' + data[p_dia]

    return form_data
