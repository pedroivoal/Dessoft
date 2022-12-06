def nota_quizzes(q1, q2, q3, q4, q5):

    q = [q1, q2, q3, q4, q5]
    menor = min(q)

    if 0<=q1<=10 and 0<=q2<=10 and 0<=q3<=10 and 0<=q4<=10 and 0<=q5<=10:
        media = (q1 + q2 + q3 + q4 + q5 - menor) / 4
    else:
        media = 0

    return media
