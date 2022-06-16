import random
def apostando_em_dados(ndado, vaposta, nrodada):
    c = 0
    while c < nrodada:
        nsorte = random.randint(1,6)
        if ndado == nsorte:
            vaposta = vaposta *  4 / 3
        if ndado != nsorte:
            vaposta = vaposta * 5/6
        print(vaposta)
        c += 1
    return vaposta