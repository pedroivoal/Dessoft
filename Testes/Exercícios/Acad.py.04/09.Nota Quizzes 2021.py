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