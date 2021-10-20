def decodifica(stri, dic):
    for k, v in dic.items():
        print(k , v)
        for letra in stri:
            print(letra)
            if letra == v:
                letra = k        
            print (letra)
    return stri

dic = {
    'a': 'z',
    'b': 'e',
    'z': '!',
    'e': '*',
}

stri = 'eznznz'

print(decodifica(stri, dic))