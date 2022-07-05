def agrupa_por_idade(grupo):

    faixas = {
        'criança': [], 
        'adolescente': [], 
        'adulto': [], 
        'idoso': []
    }


    for nome, idade in grupo.items():

        if idade <= 11:
            faixas['criança'].append(nome)
        elif idade <= 17:
            faixas['adolescente'].append(nome)
        elif idade <= 59:
            faixas['adulto'].append(nome)
        else:
            faixas['idoso'].append(nome)

    return faixas

d = {'João': 10, 'Maria': 8, 'Miguel': 20, 'Helena': 67, 'Alice': 50}
print(agrupa_por_idade(d))