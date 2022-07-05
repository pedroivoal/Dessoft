def calcula_dano(herio):

    dano = herio['força']

    for dic in herio['equipamentos']:
        dano += dic['força']

    return dano

d = {
    'nome': 'Herói',
    'força': 4,
    'vida': 25,
    'equipamentos': [
        {
            'nome': 'Martelo Mortal',
            'força': 15, 
        },
        {
            'nome': 'Luva Leve',
            'força': 2, 
        },
    ],
}
print(calcula_dano(d))