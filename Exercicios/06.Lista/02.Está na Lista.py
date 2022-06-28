def esta_na_lista(pais, l):
    
    for i in l:
        if pais == i[0]:
            return True

    return False