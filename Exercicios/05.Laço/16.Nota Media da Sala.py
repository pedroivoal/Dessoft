def nota_final(q, ai, af, ep1, ep2, pf):


    if q not in range(0, 11) or ai not in range(0, 11) or af not in range(0, 11) or ep1 not in range(0, 11) or ep2 not in range(0, 11) or pf not in range(0, 11):
        nf = 0

    else:

        ni = 0.4*ai + 0.5*af + 0.1*q

        ng = 0.1*ep1 + 0.2*ep2 + 0.7*pf

        if ni < 5 or ng < 5:
            nf = min(ni, ng)
        else:
            nf = (ni + ng)/2

    return nf

def nota_quizzes(q1, q2, q3, q4, q5):
    q = [q1, q2, q3, q4, q5]
    menor = q[0]

    for i in range(1, 5):
        if q[i] < menor:
            menor = q[i]

    media = (q1 + q2 + q3 + q4 + q5 - menor) / 4

    if q1 < 0 or q2 < 0 or q3 < 0 or q4 < 0 or q5 < 0 or q1 > 10 or q2 > 10 or q3 > 10 or q4 > 10 or q5 > 10:
        media = 0

    return media


n_alunos = 0
Sum_notas = 0
resp = 0
reprovados = 0
aprovados = 0

while resp != 'não':

    resp = input('Quer adicionar outra nota? ')
    if resp == 'não':
        break

    q1 = int(input('Quiz1: '))
    q2 = int(input('Quiz2: '))
    q3 = int(input('Quiz3: '))
    q4 = int(input('Quiz4: '))
    q5 = int(input('Quiz5: '))
    Ai = int(input('Avaliação intermediária: '))
    Af = int(input('Avaliação final: '))
    Ep1 = int(input('EP1: '))
    Ep2 = int(input('EP2: '))
    Pf = int(input('Projeto final: '))
    
    n_alunos += 1
    q = nota_quizzes(q1, q2, q3, q4, q5)
    Nf = nota_final(q, Ai, Af, Ep1, Ep2, Pf)
    Sum_notas += Nf
    
    if Nf < 5:
        reprovados += 1
    else:
        aprovados += 1

if n_alunos == 0:
    print('Média da sala: 0.00')
    print('Aprovados: 0.00%')
    print('Reprovados: 0.00%')
else:
    print('Média da sala: {:.2f}'.format    (Sum_notas/n_alunos))
    print('Aprovados: {:.2f}%'.format    (aprovados/n_alunos))
    print('Reprovados: {:.2f}%'.format    (reprovados/n_alunos))