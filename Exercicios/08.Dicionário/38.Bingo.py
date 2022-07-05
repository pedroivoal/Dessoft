def define_vencedores(n_sorteados, jogadores):

    nomes = []
    pontuacao = [0]*len(jogadores)
    vencedores = []

    i = 0
    for nome, pontos in jogadores.items():

        nomes.append(nome)
        for n in pontos:

            if n in n_sorteados:
                pontuacao[i] += 1
        i += 1

    maior = max(pontuacao)
    pontuacao.count(maior)
    i = 0
    while i < len(pontuacao):

        if pontuacao[i] == maior:
            vencedores.append(nomes[i])
        i += 1


    return vencedores

n = [1, 5, 6, 7, 9, 11, 14, 15, 16, 19]

d = {
    'joao': [4, 10, 11, 17, 19],
    'maria': [1, 4, 5, 6, 11]
}

print(define_vencedores(n, d))
