#
def apurando_votos(candidatos, votos):
    n = [0] * len(candidatos)
    cancela = 0

    i1 = 0
    while i1 < len(votos):

        m = 1
        h = 0
        i2 = 0
        while m != h and i2 < len(candidatos):
            if votos[i1] == candidatos[i2]:
                n[i2] += 1
                h += 1

            i2 += 1

        if m != h:
            cancela += 1

        i1 += 1

    iv = n.index(max(n))

    if max(n) > cancela:
        return candidatos[iv]
    else:
        return 'CANCELADA'
