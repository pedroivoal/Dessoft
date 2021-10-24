# recebe dicionario com nome dos atletas(chave) e aceleração media ao longo da corrida
def calcula_tempo(dic_atl):

    for dic_res in dic_atl:
        dic_atl[dic_res] = 10*2**(1/2)/dic_atl[dic_res]**(1/2)

    return dic_atl #devolve dicionário com nome do atleta(chave) e tempo de comclusão