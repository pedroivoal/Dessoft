def remove_vogais(text):

    new_text = ''

    for i in text:
        if i not in 'aeiouAEIOU':
            new_text += i

    return new_text

while True:

    palavra = input()
    if palavra == 'fim':
        print('Até a próxima')
        break

    palavra = remove_vogais(palavra)
    print(palavra)
