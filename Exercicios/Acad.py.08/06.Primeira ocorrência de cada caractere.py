def primeiras_ocorrencias(palavra):

    dic = {}

    for letra in palavra:
        p = palavra.find(letra)
        dic[letra] = p

    return dic

# dic_t = primeiras_ocorrencias('abracadabra')

# print(dic_t)