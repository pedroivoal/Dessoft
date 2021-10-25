# 
def calcula_media(lista_media_individual):
    c = 0
    soma = 0
    for l in lista_media_individual:
        
        for d in l.values():
            soma += d
            c += 1

    media = soma/c

    return media

# lista = [ {"aluno1": 5, "aluno2": 8}, {"aluno3": 5} ]

# m = calcula_media(lista)

# print(m)