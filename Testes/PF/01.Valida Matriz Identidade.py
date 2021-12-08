def eh_identidade(L_m):
    l = len(L_m)
    c = len(L_m[0])
    s = 0

    for i in range(0, l):

        if L_m[i][i] != 1:
            return False

        for j in range(0, c):

            s += L_m[i][j]

    if s == l and s == c:
        return True
    else:
        return False

L = [[1, 0, 0], [0, 1, 0]]

print(eh_identidade(L))