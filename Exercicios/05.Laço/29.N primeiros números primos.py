def eh_primo(num):
    z = int(num**(1/2) +1)
    if num == 1:
        return False
    elif 0 == num % 2 and num != 2:
        return False
    else:
        for i in range(3, z, 2):
            if num%i == 0:
                return False

    return True


def lista_primos(n):

    l_primos = []
    i = 2

    while len(l_primos)<n:

        bool_p = eh_primo(i)
        if bool_p:
            l_primos.append(i)

        i += 1

    return l_primos

print(lista_primos(50))