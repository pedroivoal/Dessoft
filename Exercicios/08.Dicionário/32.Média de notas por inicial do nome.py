def medias_por_inicial(D_notas):

    D_sum = {}
    D_letra = {}
    for nome, nota in D_notas.items():
        inicial = nome[0]

        if nome[0] in D_sum:
            D_sum[inicial] += nota
            D_letra[inicial] += 1
        else:
            D_sum[inicial] = nota
            D_letra[inicial] = 1

    for inicial, nota in D_sum.items():

        D_sum[inicial] = nota/D_letra[inicial]

    return D_sum

D = {'Andrew Ayres': 6, 'Fábio Ikeda': 10, 'Fábio Kurauchi': 9, 'Raul Hage': 8}
print(medias_por_inicial(D))
