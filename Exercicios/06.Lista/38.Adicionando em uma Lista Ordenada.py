
def adiciona_em_ordem(pais, dist, lista):

    lista.append([pais, dist])
    l_ordenada = [0]*len(lista)
    distancia = []

    for catalogo_pais in lista:
        distancia.append(catalogo_pais[1])

    i = 0
    while i < len(l_ordenada):

        ind = distancia.index(min(distancia))
        l_ordenada[i] = lista[ind]

        distancia.pop(ind)
        lista.pop(ind)

        i += 1
    return l_ordenada


l = [
    ['libia', 3678],
    ['franca', 3998],
    ['egito', 5008],
    ['india', 9919],
    ['japao', 13836]
]

print(adiciona_em_ordem('russia', 2425  ,l))
