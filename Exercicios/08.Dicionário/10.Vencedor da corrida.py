# recebe dicionario com nome dos atletas(chave) e aceleração media ao longo da corrida
def calcula_tempo(dic_atl):

    for dic_res in dic_atl:
        dic_atl[dic_res] = 10*2**(1/2)/dic_atl[dic_res]**(1/2)

    return dic_atl #devolve dicionário com nome do atleta(chave) e tempo de comclusão


#recebe nomes e aceleração de atletas de será digitado pelo usuario e prõe em um dicionário
dic_atl_digitados = {}
nome = ''
while nome != 'sair':
    nome = input()
    if nome != 'sair':
        ace = float(input())

    dic_atl_digitados[nome] = ace

#cria dicionario com nome dos atletas digitados(chave) e tempo de conclusão da prova
dic_atl_tempo_de_corrida = calcula_tempo(dic_atl_digitados)

#compara o tempo de conclusão de prova de todos os atletas
vencedor = ''
tempo_do_vencedor = 99999
for atleta in dic_atl_tempo_de_corrida:

    if dic_atl_tempo_de_corrida[atleta] < tempo_do_vencedor:
        tempo_do_vencedor = dic_atl_tempo_de_corrida[atleta]
        vencedor = atleta


print('O vencedor é {} com tempo de conclusão de {} s'.format(vencedor, tempo_do_vencedor))