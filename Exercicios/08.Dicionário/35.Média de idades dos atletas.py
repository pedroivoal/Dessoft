def calcula_media(D_atletas, pais):

    s = 0
    n = 0
    for inf in D_atletas.values():

        if pais == inf['nacionalidade']:
            s += inf['idade']
            n += 1

    media = s/n
    return media

d = {
    "Mathieu BILODEAU": {
        "idade": 37,
        "nacionalidade": "Canadá",
        "modalidade": "Atletismo",
    },
    "Gabriela BITOLO": {
        "idade": 22,
        "nacionalidade": "Brasil",
        "modalidade": "Handebol",
    },
    "Jerome BLAKE": {
        "idade": 25,
        "nacionalidade": "Canadá",
        "modalidade": "Atletismo",
    },
    "Felipe BORGES": {
        "idade": 36,
        "nacionalidade": "Brasil",
        "modalidade": "Handebol",
    },
    "Gabriela BRAGA GUIMARAES": {
        "idade": 26,
        "nacionalidade": "Brasil",
        "modalidade": "Vôlei",
    },
}

d  = {
    'Apriyani RAHAYU': {
        'idade': 23,
        'nacionalidade': 'Indonésia',
        'modalidade': 'Badminton'
    },
    'Luc ABALO': {
        'idade': 36,
        'nacionalidade':'França',
        'modalidade': 'Handebol'
    }, 
    'Radwa LATIF ABDEL': {
        'idade': 31, 
        'nacionalidade': 'Egito', 
        'modalidade': 'Tiro esportivo'
    }, 
    'Mohamed ABDELAAL': {
        'idade': 31,
        'nacionalidade': 'Egito', 
        'modalidade': 'Judô'
    }, 
    'Abdi ABDIRAHMAN': {
        'idade': 44, 
        'nacionalidade': 'Estados Unidos da América', 
        'modalidade': 'Atletismo'
    }, 
    'Hifumi ABE': {
        'idade': 23, 
        'nacionalidade': 'Japão', 
        'modalidade': 'Judô'
    }, 'Gunnar BENTZ': {
        'idade': 25, 
        'nacionalidade': 'Estados Unidos da América',
        'modalidade':'Nalação'
    }, 
    'Seiya ADACHI': {
        'idade': 26, 
        'nacionalidade': 'Japão', 
        'modalidade': 'Polo aquático'
    }, 
    'Morgan BARBANCON': {
        'idade': 28, 
        'nacionalidade': 'França',
        'modalidade': 'Hipismo'
    }, 
    'Guilherme BASSETO': {
        'idade': 24, 
        'nacionalidade': 'Brasil', 
        'modalidade': 'Natação'
    },
    'Shane BAZ': {
        'idade': 22, 
        'nacionalidade': 'Estados Unidos da América', 
        'modalidade': 'Beisebol'
    }, 'Bruna BENITES': {
        'idade': 35, 
        'nacionalidade': 'Brasil', 
        'modalidade': 'Futebol'}
}

print(calcula_media(d, 'Estados Unidos da América'))
