def apaga_repetidos(frase0):
    c_ja_usados = ''
    frase = ''

    for letra in frase0:

        if letra not in c_ja_usados:
            frase += letra
            c_ja_usados += letra
        else:
            frase += '*'

    return frase

print(apaga_repetidos('Um mago nunca se atrasa, nem se adianta, ele chega exatamente quando pretende chegar'))
