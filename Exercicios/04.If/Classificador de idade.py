def classifica_idade(id):
    if id < 12:
        p  = 'crianca'
    elif id < 18:
        p = 'adolescente'
    else:
        p = 'adulto'
    return p
