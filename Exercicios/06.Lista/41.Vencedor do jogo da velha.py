
def verifica_jogo_da_velha(jogo):

    # confere linhas
    for linha in jogo:
        
        if linha[0] == linha[1] == linha[2]:
            return linha[0]

    # confere colunas
    j = 0
    while j < len(jogo):

        coluna = []
        i = 0
        while i < len(jogo):

            coluna.append(jogo[i][j])

            i += 1
        j += 1

        if coluna[0] == coluna[1] == coluna[2]:
            return coluna[0]

    # confere diagonal principal
    p = 0
    diagonal = []
    while p < len(jogo):
        diagonal.append(jogo[p][p])
        p += 1

    if diagonal[0] == diagonal[1] == diagonal[2]:
            return diagonal[0]

    # confere diagonal secundária
    i = len(jogo)-1
    j = 0
    diagonal = []
    while j < len(jogo):
        diagonal.append(jogo[i][j])
        i -= 1
        j += 1
    
    if diagonal[0] == diagonal[1] == diagonal[2]:
            return diagonal[0]

    return 'V'

jogo = [
    ['X', 'O', 'X'],
    ['.', 'O', 'X'],
    ['O', '.', 'X']
]

jogo = [
    ['X', 'O', 'O'],
    ['.', 'O', 'X'],
    ['O', '.', 'X']
]

jogo = [
    ['X', '.', 'X'],
    ['X', 'O', 'O'],
    ['O', 'X', 'O']
]

print(verifica_jogo_da_velha(jogo))
