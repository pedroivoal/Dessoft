from random import choice

def sorteia_letra(palavra, restricao0):
    print(palavra)
    print(restricao0)

    simbolos =  ' !"#$%&()*+,-./:;<=>?@[\]^_`{|}~'
    restricao = ''
    sorteaveis = ''

    for letra in restricao0:
        restricao += letra
        restricao += letra.upper()

    for letra in palavra:
        
        if letra not in simbolos and letra not in restricao:
            sorteaveis += letra.lower()

    if len(sorteaveis) == 0:
        return ''
    else:
        l = choice(sorteaveis)
        return l

print(sorteia_letra('Pyongyang', ['g', 'a', 'p']))