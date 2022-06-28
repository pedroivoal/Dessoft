def eh_simetrica(matriz):

    if len(matriz) != len(matriz[0]):
        return False

    i = 0
    limite = len(matriz)
    while i < limite:

        j = 1
        while j < limite:
            elemento = matriz[i][j]
            espelho = matriz[j][i]

            if elemento != espelho:
                return False

            j += 1
        i += 1

    return True


# m = [
# [50, 52, 55], 
# [55, 56, 57], 
# [57, 58, 59]
# ]

# m = [
#     [2, -1, 5],
#     [-1, 4, 2],
#     [4, 2, -1]
# ]

# print(eh_simetrica(m))
