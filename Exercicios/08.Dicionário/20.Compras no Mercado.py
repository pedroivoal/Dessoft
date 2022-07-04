def valor_a_devolver(prateleira, caixa, compras):
    valor = 0
    for g_produto in compras:

        pp = prateleira[g_produto[0]][g_produto[1]]
        pc = caixa[g_produto[0]][g_produto[1]]

        if pp < pc:

            valor += (pc-pp)*g_produto[2]
    return valor
