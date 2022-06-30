tom_maior = [[9.9, 9.9, 10, 9.9], [10, 9.9, 9.8, 10], [10, 10, 10, 10], [10, 10, 10, 10], [10, 9.9, 9.9, 10], [9.9, 10, 10, 10], [10, 10, 9.9, 9.9], [0.0, 9.9, 10, 9.9], [10, 9.8, 10, 10]]

def calcula_escola(notas):

    s = 0
    for categoria in notas:
        s += sum(categoria) - min(categoria)

    return s

print(calcula_escola(tom_maior))