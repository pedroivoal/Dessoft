def remove_vogais(text):

    new_text = ''

    for i in text:
        if i not in 'aeiouAEIOU':
            new_text += i

    return new_text
