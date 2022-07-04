# verifica se número é primo 
def eh_primo(num):
    if num == 1:
        return False
    elif 0 == num % 2 and num != 2:
        return False
    elif 0 == num % 3 and num != 3:
        return False
    elif 0 == num % 5 and num != 5:
        return False
    elif 0 == num % 7 and num != 7:
        return False
    elif 0 == num % 11 and num != 11:
        return False
    else:
        z = int(num**(1/2) +1)
        for i in range(11, z, 2):
            if num%i == 0:
                return False
    return True

def maior_fator_primo(num0):

    num = num0
    h = 5
    primos = []
    if num%2==0:
        primos.append(2)
        while num%2==0:
            num = int(num/2)
        h= 2
    if num%3==0:
        primos.append(3)
        while num%3==0:
            num = int(num/3)
        h= 3
    if num%5==0:
        primos.append(5)
        while num%5==0:
            num = int(num/5)
        h= 5

    i = 7
    while i < int(num/h)+1:
        if num%i == 0 and eh_primo(i):

            primos.append(i)
            while num%i==0:
                num = int(num/i)
        i += 2

    # verifica se o próprio número não é primo
    # foram usadas listas no código. Para fazer sem listas bastaria ter uma variável (pmax) que guarda o maior primo
    # e ao invés do while principal ter (i < int(num/h)+1) ter (i <= num) assim bastaria retornar a variavel pmax
    # e o código abaixo se tornaria desnacessário.
    prod = 1
    for p in primos:
        prod *= p
    if prod != num:
        primos.append(num)

    return primos[-1]

# print(maior_fator_primo(5*7*67*827*4040669))
# print(5*7*67*827*4040669)
# print(maior_fator_primo(7836130001735))
print(maior_fator_primo(1836))