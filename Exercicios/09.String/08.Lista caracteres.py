def lista_caracteres(string):
    l_char = []
    for i in string:
        if i not in l_char:
            l_char.append(i)

    return l_char