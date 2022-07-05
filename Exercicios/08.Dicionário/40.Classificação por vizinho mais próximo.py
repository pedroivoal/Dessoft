def acha_distancia(x1, y1, x2, y2):
    d = ((x1-x2)**2 + (y1-y2)**2)**(0.5)
    return d

def classifica(D_fish, dim):
    menor = 10000
    x1 = dim[0]
    y1 = dim[1]

    for k in D_fish:
        size = len(D_fish[k])

        # Percorre cada dimeção de peixe conhecido
        for i in range(0, size):
            x2 = D_fish[k][i][0]
            y2 = D_fish[k][i][1]
            d = acha_distancia(x1, y1, x2, y2)

            # Atualiza menor distância 
            if d < menor:
                r = k
                menor = d

    return r
