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


l_fatores = []
def maior_fator_primo(n):
    
    if n%2 == 0:
        for i in range(n//2 - 1, n+1, 2):
            if eh_primo(i):
                l_fatores.append(i)
    elif n%2 == 1:
        for i in range(n//2 - 1, n+1, 2):
            if eh_primo(i):
                l_fatores.append(i)

    return max(l_fatores)