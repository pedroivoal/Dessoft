
b = True
lista =[]
while b:
    n = int(input('Digite um número: '))

    if n <= 0:
        b = False
    else:
        lista.append(n)

lista = sorted(lista)

print(lista)
