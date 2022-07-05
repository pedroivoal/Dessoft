def verifica_ganhador(text, D_players):
    # Configura texto para ser analisado
    text = text.lower()
    text = text.split()

    D_return = {}

    for k in D_players:
        D_return[k] = 0

        # Lê cada palavra chutada por cada jogador
        for p in D_players[k]:
            points = 0
            points += text.count(p + ',')
            points += text.count(p + '.')
            points += text.count(p + ':')
            points += text.count(p + ';')
            points += text.count(p)
            D_return[k] += points
    
    return D_return
