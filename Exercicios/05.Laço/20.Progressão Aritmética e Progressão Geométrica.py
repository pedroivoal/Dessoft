def verifica_progressao(L_n):
    r = 0

    i = 0
    while i < len(L_n)-1:
        if L_n[i] == 0:
            r -= 1
            break
        if i == 0:
            c0 = L_n[i+1]/L_n[i]
        c1 = L_n[i+1]/L_n[i]
        if c1 != c0:
            r -= 1
            break
        i += 1
    r += 1
    
    i = 0
    while i < len(L_n)-1:
        if i == 0:
            c0 = L_n[i+1]-L_n[i]
        c1 = L_n[i+1]-L_n[i]
        if c1 != c0:
            r -= 2
            break
        i += 1
    r += 2

    if r == 1:
        return 'PG'
    elif r == 2:
        return 'PA'
    elif r == 3:
        return 'AG'
    else:
        return 'NA'

# print(verifica_progressao([4,3,2,1,0,-1]))