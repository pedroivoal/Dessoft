i = 0
lista = [i]*6

while i < len(lista):
    lista[i] = int(input('Digite a nota {}:  '.format(i+1)))
    i += 1

print('Notas digitadas')

i = 0
while i < len(lista):
    print(lista[i])
    i += 1

i = 0
s = 0
while i < len(lista):
    s += lista[i]
    i += 1

media = s/(i)
print('Média: {:.2f}'.format(media))