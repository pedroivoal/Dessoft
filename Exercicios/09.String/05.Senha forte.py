def valida_senha(string):

    l_simbolos = ['?', '!', '@', '#', '$', '%', '&', '*']
    n_simbolos = 0

    if len(string)<8:
        return False

    for i in l_simbolos:
        if i in string:
            n_simbolos += 1
    if n_simbolos < 2:
        return False

    i = 0
    while i < len(string)-1:
        if string[i] == string[i+1]:
            return False
        i += 1
    
    return True
