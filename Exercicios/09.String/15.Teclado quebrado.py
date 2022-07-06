def conserta_teclado(palavra0):

    if palavra0 == '':
        return ''

    palavra0 = palavra0.lower()

    palavra = palavra0[0]
    c = palavra0[0]
    for letra in palavra0:

        if letra != c:
            c = letra
            palavra += letra

    return palavra

print(conserta_teclado('ppppppaaaaallaaavvvvrrrrrrrrrrrrraaaaa GosSssSStosaaaa'))