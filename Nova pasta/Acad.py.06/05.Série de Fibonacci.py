def calcula_fibonacci(n):
    i = 0
    lista = [0]*n
    #Faz o controle de listas vazias ou com 1 elemento
    if n > 1:
        lista[0] = 1
        lista[1] = 1
    elif n > 0:
        lista[0] = 1
    # calcula a sequência de Fibonacci
    while i < n-2:
        lista[i+2] = lista[i+1]+lista[i]
        i += 1
    return lista