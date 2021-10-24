def total_do_semestre_por_bairro(dic):
    
    dic_r = {}

    for bairo, gasto12 in dic.items():
        gasto6 = 0
        for i in range(6,12):
            gasto6 += gasto12[i]

        dic_r[bairo] = gasto6

    return dic_r

bairos = {
    'Bairro 1': [1234.45, 5123.32, 6134.35, 8567.98, 5472.28, 9715.38, 1380.15, 2569.42, 8459.24, 8351.25, 4082.19, 1750.16],
    'Bairro 2': [236.62, 845.52, 475.72, 846.22, 735.34, 846.26, 48.97, 624.37, 375.46, 4568.76, 73.32, 475.74],
    'Bairro 3': [51234.45, 5123.32, 61334.35, 8567.98, 5472.28, 9715.38, 1380.15, 2569.42, 8459.24, 82351.25, 4082.19, 1750.16],
}

print(total_do_semestre_por_bairro(bairos))