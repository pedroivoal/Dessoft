v = float(input('Valor da casa: '))
s = float(input('Salário: '))
t = float(input('Tempo em anos: '))
ve = v/t/12

if ve > 0.3*s:
    print('Empréstimo não aprovado')
else:
    print('Empréstimo aprovado')
