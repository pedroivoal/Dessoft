def lista_em_zigue_zague(seq):

    if len(seq)==0 or len(seq)==1 or len(seq)==2 and seq[0]!=seq[1]:
        return True
    elif len(seq)<=2:
        return False

    i = 0
    while i < len(seq)-2:

        if seq[i] < seq[i+1] and seq[i+2] < seq[i+1] or seq[i] > seq[i+1] and seq[i+2] > seq[i+1]:
            i += 1
        else:
            return False

    return True

# zz = [2, 1, 5, 2, 3, 1]
# print(lista_em_zigue_zague(zz))
# zz = []
# print(lista_em_zigue_zague(zz))
# zz = [1]
# print(lista_em_zigue_zague(zz))
# zz = [2, 9]
# print(lista_em_zigue_zague(zz))
# zz = [2, 1, 5, 2, 2, 3, 1]
# print(lista_em_zigue_zague(zz))
# zz = [3, 11, 2, 7, 4, 9, 11]
# print(lista_em_zigue_zague(zz))
# zz = [3, 11, 2, 7, 4, 9, 11]
# print(lista_em_zigue_zague(zz))
