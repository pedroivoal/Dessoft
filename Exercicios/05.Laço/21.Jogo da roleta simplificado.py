from random import randint

print('você tem 100 R$')
montante = 100

while True:

    aposta = int(input('aposte um valor: '))
    if aposta == 0:
        break
    tipo = input('tipo: ')

    if tipo == 'p' and aposta != 0:

        stri = input('[p/i]: ')
        s = randint(0, 36)

        if stri == 'p' and s%2 == 0 or stri == 'i' and s%2 == 1:
            montante += aposta
        else:
            montante -= aposta

    elif tipo == 'n' and aposta != 0:

        num = int(input('número da aposta? [1 à 36]: '))
        s = randint(0, 36)

        if s == num:
            montante += aposta*35
        else:
            montante -= aposta

    print()

    if montante == 0:
        break

    print(f'montante: {montante}')