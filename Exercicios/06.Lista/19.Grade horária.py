def compromisso_no_periodo(grade, dia, periodo):

    if grade[periodo][dia]!='':
        return grade[periodo][dia]
    else:
        return 'Livre'