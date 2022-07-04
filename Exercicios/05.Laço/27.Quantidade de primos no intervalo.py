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


def primos_entre(a, b):

    i = 0
    cont = a
    while cont <= b:
        
        bool_p = eh_primo(cont)
        if bool_p:
            i += 1
        cont += 1

    return i

# print(primos_entre(0, 100))