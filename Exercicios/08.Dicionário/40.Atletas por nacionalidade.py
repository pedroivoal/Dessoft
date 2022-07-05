def agrupa_por_nacionalidade(atletas):

    nacionalidades = {}
    for atleta, inf in atletas.items():

        if inf['nacionalidade'] in nacionalidades:
            nacionalidades[inf['nacionalidade']].append(atleta)
        else:
            nacionalidades[inf['nacionalidade']] = [atleta]

    return nacionalidades

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
        "idade": 27,
        "nacionalidade": "Brasil",
        "modalidade": "Vôlei",
    },
}

print(agrupa_por_nacionalidade(d))