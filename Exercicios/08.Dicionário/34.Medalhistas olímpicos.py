def mais_medalhas(L0):

    i = 0
    for dic in L0:

        if i == 0:
            nacionalidade = dic['nacionalidade']
            n_ouros = dic['ouro']
            i += 1
        else:
            if dic['ouro'] > n_ouros:
                n_ouros = dic['ouro']
                nacionalidade = dic['nacionalidade']

    return nacionalidade

l = [{
    'nome': ' Michael Phelps',
    'nacionalidade': 'Norte Americano',
    'ouro': 23, 'prata': 3, 'bronze': 2,
},
{
    'nome': 'Larisa Latynina',
    'nacionalidade': 'Russo',
    'ouro': 9, 'prata': 5, 'bronze': 4,
},
{
    'nome': 'Nikolai Andrianov',
    'nacionalidade': 'Russo',
    'ouro': 7, 'prata': 5, 'bronze': 3,
},
{
    'nome': 'Boris Shakhlin',
    'nacionalidade': 'Russo',
    'ouro': 7, 'prata': 4, 'bronze': 2,
},
{
    'nome': 'Jenny Thompson',
    'nacionalidade': 'Norte Americano',
    'ouro': 8, 'prata': 3, 'bronze': 1,
}]

print(mais_medalhas(l))
print(len(l))