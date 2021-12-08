# recebe salário da pessoa
# retorna valor da contribuição para o INSS
def INSS_table(salary):

    if salary < 1045.01:
        tax = salary*0.075
    elif salary < 2089.61:
        tax = salary*0.09
    elif salary < 3134.41:
        tax = salary*0.12
    elif salary < 6101.07:
        tax = salary*0.14
    else:
        tax = 671.12

    return tax

# recebe base de cálculo da pessoa
# retorna alícota e dedução(numa lista, nessa ordem)
def calc_base_table(calc_base):

    if calc_base < 1903.99:
        al = 0
        ded = 0
    elif calc_base < 2826.66:
        al = 0.075
        ded = 142.80
    elif calc_base < 3751.06:
        al = 0.15
        ded = 354.80
    elif calc_base < 4664.68:
        al = 0.225
        ded = 636.13
    else:
        al = 0.275
        ded = 869.36

    return [al, ded]


salary = float(input())
dependets = float(input())

calc_base = salary - INSS_table(salary) - dependets*189.59

IRRF = calc_base*calc_base_table(calc_base)[0] - calc_base_table(calc_base)[1]

if IRRF == -0.0:
    IRRF = 0

print(IRRF)