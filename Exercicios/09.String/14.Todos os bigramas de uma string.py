def acha_bigramas(string):

    bigramas = []
    i = 0
    while i < len(string)-1:

        bigrama = string[i:i+2]

        if bigrama not in bigramas:
            bigramas.append(bigrama)

        i += 1

    return bigramas


print(acha_bigramas('babador'))
