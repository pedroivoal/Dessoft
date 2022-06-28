def calcula_total_da_nota(preco, quantidade):
    valor_total = 0
    i = 0
    while i < len(preco):
        valor_total += preco[i] * quantidade[i]
        i += 1

    return valor_total
