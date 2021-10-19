def valida_data(dia, mes, ano):

    # ano bissexto
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:

        # janeiro
        if mes == 1:

            if dia > 0 and dia < 32:
                res = True
            else:
                res = False

        # fevereiro
        elif mes == 2:

            if dia > 0 and dia < 30:
                res = True
            else:
                res = False

        # março
        elif mes == 3:

            if dia > 0 and dia < 32:
                res = True
            else:
                res = False

        # abriu
        elif mes == 4:

            if dia > 0 and dia < 31:
                res = True
            else:
                res = False

        # maio
        elif mes == 5:

            if dia > 0 and dia < 32:
                res = True
            else:
                res = False

        # junho
        elif mes == 6:

            if dia > 0 and dia < 31:
                res = True
            else:
                res = False

        # julho
        elif mes == 7:

            if dia > 0 and dia < 32:
                res = True
            else:
                res = False

        # agosto
        elif mes == 8:

            if dia > 0 and dia < 32:
                res = True
            else:
                res = False

        # setembro
        elif mes == 9:

            if dia > 0 and dia < 31:
                res = True
            else:
                res = False

        # outubro
        elif mes == 10:

            if dia > 0 and dia < 32:
                res = True
            else:
                res = False

        # novembro
        elif mes == 11:

            if dia > 0 and dia < 31:
                res = True
            else:
                res = False

        # dezembro
        elif mes == 12:

            if dia > 0 and dia < 32:
                res = True
            else:
                res = False

        # mês inválido
        else:
            res = False


    # ano não bissexto
    else:

        # janeiro
        if mes == 1:

            if dia > 0 and dia < 32:
                res = True
            else:
                res = False

        # fevereiro
        elif mes == 2:

            if dia > 0 and dia < 29:
                res = True
            else:
                res = False

        # março
        elif mes == 3:

            if dia > 0 and dia < 32:
                res = True
            else:
                res = False

        # abriu
        elif mes == 4:

            if dia > 0 and dia < 31:
                res = True
            else:
                res = False

        # maio
        elif mes == 5:

            if dia > 0 and dia < 32:
                res = True
            else:
                res = False

        # junho
        elif mes == 6:

            if dia > 0 and dia < 31:
                res = True
            else:
                res = False

        # julho
        elif mes == 7:

            if dia > 0 and dia < 32:
                res = True
            else:
                res = False

        # agosto
        elif mes == 8:

            if dia > 0 and dia < 32:
                res = True
            else:
                res = False

        # setembro
        elif mes == 9:

            if dia > 0 and dia < 31:
                res = True
            else:
                res = False

        # outubro
        elif mes == 10:

            if dia > 0 and dia < 32:
                res = True
            else:
                res = False

        # novembro
        elif mes == 11:

            if dia > 0 and dia < 31:
                res = True
            else:
                res = False

        # dezembro
        elif mes == 12:

            if dia > 0 and dia < 32:
                res = True
            else:
                res = False

        # mês inválido
        else:
            res = False

    return res