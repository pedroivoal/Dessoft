
def calcula_troco(pago_pelo_cliente, preco_dos_produtos, notas):

    troco = preco_dos_produtos - pago_pelo_cliente
    l_n_troco = []

    for nota in notas:
        l_n_troco.append(int(troco//nota))
        troco = troco%nota

    mensagens = [' nota(s) de R$ ', ' moeda(s) de R$ ']
    l_mensagens = []

    i = 0
    while i < len(l_n_troco):
        if l_n_troco[i] != 0:
            if notas[i] == int(notas[i]) and notas[i]!=1:
                l_mensagens.append(str(l_n_troco[i]) + mensagens[0] + str(notas[i]))
            else:
                l_mensagens.append(str(l_n_troco[i]) + mensagens[1] + str(notas[i]))
        i += 1

    return l_mensagens

# notas = [100, 50, 20, 10, 5, 2, 1, 0.5, 0.25, 0.1, 0.05]
# print(calcula_troco(2587.96487, 43986.2456, notas))
