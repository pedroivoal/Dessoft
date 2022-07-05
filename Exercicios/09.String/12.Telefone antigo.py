def atualiza_telefone(telefone):

    t = telefone.find('-')
    if t == -1:
        if len(telefone) == 8:
            telefone = '9'+telefone
    else:
        if len(telefone) == 9:
            telefone = '9'+telefone
    
    return telefone
