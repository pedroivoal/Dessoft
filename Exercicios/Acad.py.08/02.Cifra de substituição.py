def decodifica(stri, dic):
    i = 0
    for cod in dic:

        while i < len(stri):

            if dic[cod] == stri[i]:
                stri.replace(stri[i], cod)
            i += 1

    return stri

dic = {
    'a': 'z',
    'b': 'e',
    'z': '!',
    'e': '*',
}

stri = 'eznznz'

print(decodifica(stri, dic))