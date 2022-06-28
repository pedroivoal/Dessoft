def eh_fibonacci(lista):

    #confere se alista tem mais que 2    
    #valores
    if len(lista) > 2:

        #confere o padrão de Fibonacci em
        #toda a lista
        i = 0
        while i < len(lista)-2:
            k = lista[i]+lista[i+1]-lista[i+2]
            if k != 0:
                break
            
            i += 1

        #retorna a saida de acordo com o 
        #valor da constante "k"
        if k == 0:
            saida = True
        else:
            saida = False

    else:
        saida = False
    
    return saida
    