def calcula_tempo(dic_atl):

    for dic_res in dic_atl:
        dic_atl[dic_res] = 10*2**(1/2)/dic_atl[dic_res]**(1/2)

    return dic_atl