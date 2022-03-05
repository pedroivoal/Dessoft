def quadrados_no_intervalo(a, b):

    r = 0
    i = a
    while i in range(a, b+1):

        if i**(1/2) == int(i**(1/2)):
            r += 1
        
        i += 1

    return r