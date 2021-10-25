# 
def notas_dp(notas):

    lista_dp = []

    for dic_al in notas:
        pi = dic_al['PI']
        pf = dic_al['PF']
        nf = (pi+pf)/2

        if nf < 5:
            lista_dp.append(dic_al['matricula'])

    return lista_dp
    



notas = [

{'matricula' : 123, 'PI' : 7, 'PF': 3},

{'matricula' : 456, 'PI': 4, 'PF': 8},

{'matricula' : 789, 'PI': 5, 'PF': 1}

]

print(notas_dp(notas))