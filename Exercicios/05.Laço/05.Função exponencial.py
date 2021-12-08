import math

def calcula_euler (x, n):
    soma = 0
    i = 1
    while i <= n-1:
        soma +=  x**(i)/math.factorial(i)
        i += 1

    ex  = soma + 1

    return ex

print(calcula_euler(1,10))