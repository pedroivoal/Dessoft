def total_centro_custo(D_e):
    D_return = {}

    # Pecorre dados de cada pessoa
    for v in D_e.values():

        if v['centro de custo'] not in D_return:
            D_return[v['centro de custo']] = 0
        
        D_return[v['centro de custo']] += v['valor']
    
    return D_return
