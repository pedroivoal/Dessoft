def aniversariantes_de_setembro(D_aniversario):

    D_setembro = {}

    for nome, aniversario in D_aniversario.items():

        if aniversario[3:5]=='09':

            D_setembro[nome] = aniversario

    return D_setembro
