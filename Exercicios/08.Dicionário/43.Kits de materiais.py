from traceback import print_tb


def separa_por_inicial(turmas):

    inicial_nomes = {}

    for alunos in turmas.values():

        for aluno in alunos:
            
            if aluno[0] in inicial_nomes:
                inicial_nomes[aluno[0]].append(aluno)
            else:
                inicial_nomes[aluno[0]] = [aluno]

    return inicial_nomes

d = {
    "Turma A": ["Ana", "Beatriz", "Jorge"],
    "Turma B": ["Cecília", "João"],
    "Turma C": ["Amanda", "Joana", "Lucas"],
}
print(separa_por_inicial(d))