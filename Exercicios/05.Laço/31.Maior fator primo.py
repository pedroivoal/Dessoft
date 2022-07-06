def maior_fator_primo(num0):

    num = num0
    primos = []
    if num%2==0:
        primos.append(2)
        while num%2==0:
            num = int(num/2)

    i = 3
    while i < int(num/2)+1:

        if num%i == 0:
            
            primos.append(i)
            while num%i==0:
                num = int(num/i)
        i += 2

    # foram usadas listas no código. Para fazer sem listas bastaria ter uma variável (pmax) que guarda o maior primo
    # e ao invés do while principal ter (i < int(num/h)+1) ter (i <= num) assim bastaria retornar a variavel pmax
    # e o código abaixo se tornaria desnacessário.

    # verifica se o próprio número não é primo
    prod = 1
    for p in primos:
        prod *= p
    if prod != num:
        primos.append(num)

    return max(primos)

# print(maior_fator_primo(5*7*67*827*4040669))
# print(5*7*67*827*4040669)
# print(maior_fator_primo(7836130001735))