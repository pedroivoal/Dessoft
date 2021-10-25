def pedra_papel_tesoura(j1, j2):

    if j1 not in ["pedra","papel","tesoura"] or j2 not in ["pedra","papel","tesoura"]:
        ret = "Escolha pedra, papel ou tesoura para jogar"
    else:
        if (j1 == 'pedra' and j2 == 'tesoura') or (j1 == 'papel' and j2 == 'pedra') or (j1 == 'tesoura' and j2 == 'papel'):
            ret = 'um'
        elif (j2 == 'pedra' and j1 == 'tesoura') or (j2 == 'papel' and j1 == 'pedra') or (j2 == 'tesoura' and j1 == 'papel'):
            ret = 'dois'
        else:
            ret = 'empate'
        
    return ret