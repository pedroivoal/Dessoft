#
def calcula_investimento(inv, mes, tipo):
    # seleciona tipo de investimento

    # CDB
    if tipo == 'CDB':

        for i in range(1, mes + 1):
            inv = inv * 1.013

            if i % 6 == 0:
                inv = inv * 1.012

    # LCI
    elif tipo == 'LCI':
        inv  = inv*1.016**(mes)
        '''for i in range(1, mes + 1):
            inv = inv * 1.016'''

    # LCA
    else:

        for i in range(1, mes + 1):
            inv = inv * 1.0145

            if i % 4 == 0:
                inv = inv * 1.01

    return inv