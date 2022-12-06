from math import e

lamb = float(input("Qual a taxa (λ)? "))
x = float(input("Qual x, para calcular F(λ, x)? "))

f = 1-e**(-lamb*x)

print(f'{f:.4f}')
