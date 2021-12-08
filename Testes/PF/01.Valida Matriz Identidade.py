def eh_identidade(L_m):
    l = len(L_m) # Número de linhas
    c = len(L_m[0]) # Número de colunas
    s = 0

    # Percorre cada linha
    for i in range(0, l):

        # Confere se havia o número 1 em cada casa da diagonal principal
        if L_m[i][i] != 1:
            return False

        # Percorre os valores de cada linha
        for j in range(0, c):

            s += L_m[i][j]

    # Confere se havia apenas o número 1 na diagonal principal
    if s == l and s == c:
        return True
    else:
        return False

# L = [[1, 0, 0], [0, 1, 0], [0, 0, 1]]

# print(eh_identidade(L))