
def eh_primo(num):
    c = 0
    z = int(num**(1/2) +1)#acha o maior valor(sem conta o próprio número) que dividiria o número caso ele não fosse primo.
    if num == 1:
        return False
    elif 0 == num % 2 and num != 2:
        return False
    else:
        for i in range(3, z, 2):
            if num%i == 0:
                return False

    return True

# n = int(input())
# print(eh_primo(n))