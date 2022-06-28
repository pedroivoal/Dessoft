def quantos_caminhoes(pesos):
    
    n_caminhoes = 0
    p_caminhao = 0
    for peso in pesos:

        if p_caminhao + peso < 2000:
            p_caminhao += peso
        elif p_caminhao + peso == 2000:
            p_caminhao = 0
            n_caminhoes += 1
        else:
            p_caminhao = peso
            n_caminhoes += 1

    if p_caminhao != 0:
        n_caminhoes += 1

    return n_caminhoes

print(quantos_caminhoes([1000, 500, 400, 200, 50, 450, 1300, 500, 1450, 100]))
