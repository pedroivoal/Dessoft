
def eh_primo(num):

    if num < 0:
        return False

    if num == 1:
        return False
    elif 0 == num % 2 and num != 2:
        return False
    else:
        z = int(num**(1/2) +1)
        for i in range(3, z, 2):
            if num%i == 0:
                return False

    return True


def primos_entre(a, b):

    primos = []
    i = a
    if a%2==0 and i != 2 and i > 2:
        i += 1
    elif i<=2:
        primos.append(2)
        i += 1
    while i <= b:

        if eh_primo(i):
            primos.append(i)
        i += 2
    return primos

