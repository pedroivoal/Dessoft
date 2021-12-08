from math import sqrt

def calcula_pi(n):
    s = 0
    i = 1
    while i<=n:
        s += 6/i**2
        i += 1
    res = sqrt(s)
    return res

rf = calcula_pi(70)
print(rf)
