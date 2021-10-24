#
def nivel_idh(idh):
    # seleciona nível do IDH
    if idh < 0.350:
        nivel = 'Sem dados'
    elif idh < 0.555:
        nivel = 'Baixo'
    elif idh < 0.700:
        nivel = 'Médio'
    elif idh < 0.800:
        nivel = 'Alto'
    else:
        nivel = 'Muito Alto'

    return nivel