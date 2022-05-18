
def palavras_sao_iguais(string):
    l = string.split('-')
    if '-' in string:
        if l[0]==l[1]:
            return True
        return False
    return False