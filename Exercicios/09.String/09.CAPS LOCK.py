def capsLock(text):
    new_tetx = ''
    for i in text:
        if i in 'abcdefghijklmnopqrstuvwxyz':
            new_tetx += i.upper()
        elif i in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
            new_tetx += i.lower()
        else:
            new_tetx += i

    return new_tetx