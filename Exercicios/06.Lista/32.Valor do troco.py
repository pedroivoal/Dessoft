
def calcula_troco(preco, recebido, notas):

    troco = preco - recebido
    l_n_troco = []

    i = 0
    while i < 11:
        x = (troco - troco%notas[i])/notas[i]
        if x < 0:
            x = 0
        l_n_troco.append(int(troco//notas[i]))
        troco = troco%notas[i]
        i += 1
        print(l_n_troco)

    mensagens = [' nota(s) de R$ ', ' moeda(s) de R$ ']
    l_mensagens = []

    i = 0
    while i < len(l_n_troco):
        if l_n_troco[i] != 0:
            if i < 6:
                l_mensagens.append(str(l_n_troco[i]) + mensagens[0] + str(notas[i]))
            else:
                l_mensagens.append(str(l_n_troco[i]) + mensagens[1] + str(notas[i]))
        i += 1

    return l_mensagens

notas = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05]
print(calcula_troco(86.5, 10, notas))
