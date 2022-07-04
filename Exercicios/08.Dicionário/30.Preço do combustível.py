def contabiliza_combustivel(D0):

    D_return = {}

    for dia in D0.values():

        if dia['tipo'] in D_return:
            D_return[dia['tipo']]['total litros'] += dia['litros']
            D_return[dia['tipo']]['custo por litro'] += dia['custo']
        else:
            D_return[dia['tipo']] = {
                'total litros': dia['litros'],
                'custo por litro': dia['custo']
            }

    for tipo, dados in D_return.items():
        D_return[tipo]['custo por litro'] = dados['custo por litro']/dados['total litros']

    return D_return


{
    'Etanol': {
        'total litros': 50,
        'custo por litro': 2.4
    },
    'Gasolina': {
        'total litros': 40,
        'custo por litro': 5
    }
}


D = {
    'dia 1': {
        'tipo': 'Etanol',
        'litros': 20,
        'custo': 50.0
    },
    'dia 4': {
        'tipo': 'Gasolina',
        'litros': 25,
        'custo': 150.5
    },
    'dia 10': {
        'tipo': 'Gasolina',
        'litros': 15,
        'custo': 49.5
    },
    'dia 14': {
        'tipo': 'Etanol',
        'litros': 30,
        'custo': 70.0
    }
}

print(contabiliza_combustivel(D))
