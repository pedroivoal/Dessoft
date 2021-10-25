#recebe uma lista de palavras
#retorna dicionário com palavras(chave) e seu número de aparições
def conta_ocorrencias(lista_de_palavras):

    dic_numero_de_palavras = {}

    #adiciona cada palavra ao dicionário
    for palavra in lista_de_palavras:
        dic_numero_de_palavras[palavra] = 0
    
    #conta o número de apariçõe da palavra
    for palavra in lista_de_palavras:
        dic_numero_de_palavras[palavra] += 1

    return dic_numero_de_palavras


# lista = ['abobora', 'chuchu', 'abobora', 'abobora', 'chuchu']

# print(conta_ocorrencias(lista))
#{'chuchu': 2, 'abobora': 3}