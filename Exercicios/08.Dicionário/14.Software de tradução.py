#recebe lista de palavras em ingles e dicionario com palavra em ingles(chave) e tradução em portugues
#retorna lista de palavras em português
def traduz(list_in_eng, dic_translation):

    list_in_port = []

    for word in list_in_eng:
        list_in_port.append(dic_translation[word])
    
    return list_in_port
