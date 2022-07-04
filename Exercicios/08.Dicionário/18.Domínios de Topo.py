def usuarios_por_pais(L_usuarios, D_nacoes):

    D_return0 = {}
    for v in D_nacoes.values():
    
        D_return0[v] = []

    for usuario in L_usuarios:

        nome_usuario = ''
        i = 0
        while usuario[i] != '@':
            nome_usuario += usuario[i]
            i += 1

        nacao = usuario[-2:]

        D_return0[D_nacoes[nacao]].append(nome_usuario)

    D_return = {}
    for k, v in D_return0.items():
        if v != []:
            D_return[k] = v

    return D_return


l = ['usuario1@insper.edu.br', 'usuario2@uma.pt', 'usuario3@kth.se', 'usuario4@usp.br']
d = {
    'pt': 'Portugal',
    'br': 'Brasil',
    'se': 'Suécia',
    'tu': 'Tunuvalu'
}

print(usuarios_por_pais(l, d))
