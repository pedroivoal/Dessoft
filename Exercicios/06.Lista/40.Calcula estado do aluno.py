def media(quizzes, provas):
    media_q = (sum(quizzes)-min(quizzes))/(len(quizzes)-1)
    media = 0.1*media_q + 0.4*provas[0] + 0.5*provas[1]

    return media


def calcula_estado(lista):

    estado = []

    for aluno in lista:

        med = media(aluno[1], aluno[2])
        if med >= 5:
            estado.append([aluno[0],'A'])
        elif med <= 5:
            estado.append([aluno[0],'R'])

    return estado



notas = [
    ['Maria', [5.0, 10.0, 0.0, 10.0, 10.0], [6.7, 8.0]],
    ['Joao', [0.0, 10.0, 10.0, 10.0, 0.0], [6.7, 2.0]],
    ['Joana', [10.0, 0.0, 10.0, 0.0, 10.0], [6.7, 8.0]]
]

print(calcula_estado(notas))