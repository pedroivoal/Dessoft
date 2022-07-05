def perfis_profissionais(funcionarios):

    censo = {}
    lr = []
    ln = []

    for informacoes in funcionarios.values():

        ramo = informacoes['ramo']
        if ramo not in lr:
            lr.append(ramo)
        if lr.index(ramo) < len(ln):
            ln[lr.index(ramo)] += 1
        else:
            ln.append(1)

        if ramo in censo:
            censo[ramo]['média salarial'] += informacoes['salário']
            censo[ramo]['tempo médio de serviço'] += informacoes['anos de serviço']

            i = informacoes['e-mail'].find('@')+1
            servidor = ''
            while informacoes['e-mail'][i]!= '.':
                servidor += informacoes['e-mail'][i]
                i += 1
            if servidor not in censo[ramo]['servidores']:
                censo[ramo]['servidores'].append(servidor)

        else:
            censo[ramo] = {
                'média salarial': informacoes['salário'],
                'tempo médio de serviço': informacoes['anos de serviço'],
                'servidores': []
            }

            i = informacoes['e-mail'].find('@')+1
            servidor = ''
            while informacoes['e-mail'][i]!= '.':
                servidor += informacoes['e-mail'][i]
                i += 1
            censo[ramo]['servidores'].append(servidor)

    for ramo in censo:

        n = ln[lr.index(ramo)]

        censo[ramo]['média salarial'] = censo[ramo]['média salarial']/n
        censo[ramo]['tempo médio de serviço'] = censo[ramo]['tempo médio de serviço']/n

    return censo

{
      'secretariado': {
          'média salarial': 3750,
          'tempo médio de serviço': 4,
          'servidores': ['hotmail','uol']
      },
      'odontologia': {
          'média salarial': 7500,
          'tempo médio de serviço': 9,
          'servidores': ['gmail']
      },
      'vendas': {
          'média salarial': 4000,
          'tempo médio de serviço': 2,
          'servidores': ['yahoo']
      }
  }

d = {
    'Pedro Souza': {
        'ramo': 'secretariado',
        'salário': 2500,
        'anos de serviço': 3,
        'e-mail': 'pedro.paulo@hotmail.com'
    },
    'Marisa Monteiro': {
        'ramo': 'odontologia',
        'salário': 6000,
        'anos de serviço': 8,
        'e-mail': 'marisa_monteiro@gmail.com'
    },
    'Vitor Cerqueira': {
        'ramo': 'odontologia',
        'salário': 9000,
        'anos de serviço': 10,
        'e-mail': 'vitorcerqueira@gmail.com'
    },
    'Sandra Gomes': {
        'ramo': 'secretariado',
        'salário': 5000,
        'anos de serviço': 5,
        'e-mail': 'gomes-sandra@uol.com.br'
    },
    'Patrícia Ramos': {
        'ramo': 'vendas',
        'salário': 4000,
        'anos de serviço': 2,
        'e-mail': 'patricia-ramos-1990@yahoo.com.br'
    }
}

print(perfis_profissionais(d))
