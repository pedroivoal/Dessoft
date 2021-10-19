import random

def apostando_em_dados(ndado, vaposta, nrodada):
    c = 1
    while c <= nrodada:
        nsorte = random.randint(1,6)
        if ndado == nsorte:
            vaposta = vaposta *  4 / 3
        if ndado != nsorte:
            vaposta = vaposta * 5/6
        print(c,'-', vaposta)
        c += 1
    return vaposta

ndado = int(input('Digite o número do dado: ' ))
vaposta =  int(input('Digite o valor a ser apostado: '))
nrodada = int(input('Digite o número de rodadas: '))
res = apostando_em_dados(ndado, vaposta, nrodada)
