def quadrado_magico(quadrado):

    valor0 = sum(quadrado[0])

    # confere soma das linhas
    for linha in quadrado:
        s = sum(linha)
        if s != valor0:
            return False

    # confere soma das colunas
    i = 0
    while i < len(quadrado):

        s = 0
        j = 0
        while j < len(quadrado):

            s += quadrado[i][j]

            j += 1
        i += 1

        if s != valor0:
            return False

    # confere soma da diagonal principal
    p = 0
    s = 0
    while p < len(quadrado):
        s += quadrado[p][p]
        p += 1

    if s != valor0:
        return False

    # confere soma da diagonal secundária
    i = len(quadrado)-1
    j = 0
    s = 0
    while j < len(quadrado):
        s += quadrado[i][j]
        i -= 1
        j += 1
    
    if s != valor0:
        return False

    return True

M = [[2, 7, 6], [9, 5, 1], [4, 3, 8]]

print(quadrado_magico(M))