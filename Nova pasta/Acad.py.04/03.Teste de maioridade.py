def verifica_idade(id):
    if id >= 21:
        pri = 'Liberado EUA e BRASIL'
    elif id >= 18:
        pri = 'Liberado BRASIL'
    else:
        pri = 'Não está liberado'
    return pri