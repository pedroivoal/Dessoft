# 
def valida_data(dia, mes, ano):

    # ano bissexto
    if ano % 4 == 0 and ano % 100 != 0 and mes == 2 or ano % 400 == 0 and mes == 2:

        # fevereiro
        if dia > 0 and dia < 30:
            return True
        else:
            return False

    # ano não bissexto
    else:

        # janeiro, março, maio, julho, agosto, outubro, dezembro
        if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:

            if dia > 0 and dia < 32:
                return True
            else:
                return False

        # fevereiro
        elif mes == 2:

            if dia > 0 and dia < 29:
                return True
            else:
                return False

        # abriu, junho, setembro, novembro
        elif mes == 4 or mes == 6 or mes == 9 or mes == 11:

            if dia > 0 and dia < 31:
                return True
            else:
                return False

        # mês inválido
        else:
            return False