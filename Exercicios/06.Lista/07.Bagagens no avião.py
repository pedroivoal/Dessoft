def filtra_bagagens(lista, altura, largura, profundidade):

    cont = 0
    
    for elemento in lista:

        b0 = elemento[0] > altura
        b1 = elemento[1] > largura
        b2 = elemento[2] > profundidade

        if b0 or b1 or b2:

            cont += 1

    return cont