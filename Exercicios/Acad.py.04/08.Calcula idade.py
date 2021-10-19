def calcula_idade(d1=21,m1=20,a1=1,d2=20,m2=20,a2=40):
    res = 0
    if m1 < m2:
        res = a2 - a1
    elif d1 <= d2:
        if m1 == m2:
            res = a2 - a1
        else:
            res = a2-a1-1
    else:
        res = a2 - a1 - 1
    return res