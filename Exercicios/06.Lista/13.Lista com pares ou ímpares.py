def verifica_lista(lista):

    impar = 0
    par = 0

    for i in lista:
        
        if i%2 == 0:
            par += 1
        else:
            impar += 1

    if impar > 1 and par == 0:
        return 'ímpar'
    elif par > 1:
        return 'par'
    else:
        return 'misturado'
