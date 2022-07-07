def anagrama(palavra1, palavra2):

    letra_unica = ''
    for letra in palavra1:
        if letra not in letra_unica:
            letra_unica += letra

    for letra in letra_unica:

        q1 = palavra1.count(letra)
        q2 = palavra2.count(letra)

        if q1 != q2:
            return False

    return True

print(anagrama('alegria', 'galeria'))