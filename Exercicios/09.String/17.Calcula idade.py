def calcula_idade(nascimento, atual):

    ano_n = int(nascimento[-4:])
    mes_n = int(nascimento[3:5])
    dia_n = int(nascimento[0:2])

    ano_a = int(atual[-4:])
    mes_a = int(atual[3:5])
    dia_a = int(atual[0:2])

    if mes_n < mes_a:
        idade = ano_a - ano_n
    elif mes_n == mes_a and dia_n <= dia_a:
        idade = ano_a - ano_n
    else:
        idade = ano_a - ano_n - 1
    
    return idade


# print(calcula_idade('15/07/2000' , '13/06/2021'))
# print(calcula_idade('15/07/2000' , '20/09/2021'))
# print(calcula_idade('14/02/1989' , '14/02/2021'))
