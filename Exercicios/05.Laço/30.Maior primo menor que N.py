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


def maior_primo_menor_que(n):

    primo = -1
    i = 2

    while i<=n:

        bool_p = eh_primo(i)
        if bool_p:
            primo = i

        i += 1

    return primo