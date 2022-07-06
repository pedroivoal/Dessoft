def classifica_rima(r1, r2, r3, r4):

    if r1==r3 and r2==r4 and r1!=r2:
        return 'alternada'
    elif r1==r4 and r2==r3 and r1!=r2:
        return 'interpolada'
    elif r1==r2 and r3==r4 and r1!=r3:
        return 'emparelhada'
    else:
        return 'outra'
