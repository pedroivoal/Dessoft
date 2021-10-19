def calcula_aumento(s):
    if s > 1250:
        sn = s*1.1
    else:
        sn = 1.15*s
    return sn - s