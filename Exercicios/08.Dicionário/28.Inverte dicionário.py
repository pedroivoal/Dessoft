from numpy import sort


def inverte_dicionario(D0):

    D_inv = {}

    for nome, idade in D0.items():
        
        if idade in D_inv:
            D_inv[idade].append(nome)
        else:
            D_inv[idade] = [nome]

    return D_inv

D = {'Ana': 19, 'Bruno': 18, 'João': 19}

print(inverte_dicionario(D))