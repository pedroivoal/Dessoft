
def eh_primo(num):

    if num < 0:
        return False

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

    primos = []
    i = a
    while i <= b:

        if eh_primo(i):
            primos.append(i)
        i += 1
    return primos

print(primos_entre(-100, 101))
