def decimal_para_binario(n):

    if n < 0:
        return 'Negativo'

    binario = ''
    quociente = n
    while quociente != 0:
        binario += str(quociente%2)
        quociente = quociente//2

    return binario[::-1]

# print(decimal_para_binario(10))