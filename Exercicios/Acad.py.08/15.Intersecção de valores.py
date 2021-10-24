def interseccao_valores(dic1, dic2):

    l_intecessao_de_valores = []

    for value1 in dic1.values():

        if value1 in dic2.values():
            l_intecessao_de_valores.append(value1)

    return l_intecessao_de_valores

dic1  = {
    'A':1,
    'B':2,
    'C':3,
    'D':4,
}

dic2 = {
    'E':3,
    'F':4,
    'G':5,
    'H':6,
}

print(interseccao_valores(dic1, dic2))