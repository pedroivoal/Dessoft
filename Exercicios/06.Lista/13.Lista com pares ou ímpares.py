def verifica_lista(lista):

    impar = 0
    par = 0

    for i in lista:
        
        if i%2 == 0:
            par += 1
        else:
            impar += 1

    if impar > 0 and par == 0:
        return 'ímpar'
    elif par > 0 and impar == 0:
        return 'par'
    else:
        return 'misturado'

print(verifica_lista([1, 5, 2, 7, 3, 7, 4]))