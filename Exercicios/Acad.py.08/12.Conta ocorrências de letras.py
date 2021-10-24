def conta_letras(string):

    dic_letters = {}
    for letter in string:
        dic_letters[letter] = 0
    
    for letter in string:
        dic_letters[letter] += 1

    return dic_letters
