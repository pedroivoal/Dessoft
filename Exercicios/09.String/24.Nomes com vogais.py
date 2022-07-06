def nomes_com_vogais(nomes):

    contador = [0, 0]
    vogais = 'AEIOU'

    for nome in nomes:

        if nome[0] in vogais:
            contador[0] += 1
        else:
            contador[1] += 1
    
    return contador
