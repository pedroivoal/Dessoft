def decodifica(stri, dic):

    dic_inv = {}
    for k, v in dic.items():
        dic_inv[v] = k

    palavra = ''
    for letra in stri:
        if letra in dic_inv:
            palavra += dic_inv[letra]

        elif letra not in dic_inv:
            palavra += letra

    return palavra