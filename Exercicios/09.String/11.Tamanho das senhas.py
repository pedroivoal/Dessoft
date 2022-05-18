def tamanho_minimo(text, n):

    r =[]
    l_pass_word = text.split()

    for i in l_pass_word:
        if len(i) > n:
            r.append(i)
    
    return r

# print(tamanho_minimo("frase para a função que filtra as palavras", 5))