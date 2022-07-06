def palavras_com_tamanho_crescente(l):

    i = 0
    while i < len(l)-1:
        if len(l[i]) >= len(l[i+1]):
            return False
        i += 1

    return True
