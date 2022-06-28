
def encontra_maximo(matriz0):

    matriz = []
    for linha0 in matriz0:
        linha = []
        for i in linha0:
            if i < 0:
                linha.append(-i)
            else:
                linha.append(i)
        matriz.append(linha)

    maiores = []
    for linha in matriz:
        maiores.append(max(linha))
    maior = max(maiores)

    return maior

print(encontra_maximo([[-1, -8978, 500], [-4, -5, -97766], [-7, -8, -9]]))


# def maior_v(linha):
#     ma = linha[0]
#     i = 1
#     while i < 3:
#         if abs(linha[i]) > ma:
#             ma = abs(linha[i])
#         i += 1
#     return ma



# def encontra_maximo(matriz):
#     maiores = []
#     for linha in matriz:
#         maiores.append(maior_v(linha))
#     maior = maior_v(maiores)
#     return maior
