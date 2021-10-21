def conta_a(palavra):

    c = 0
    for letra in palavra:

        if letra == 'a':
            c += 1
    
    return c
s = 'Insper'
r = s[::-2]
print(r)
