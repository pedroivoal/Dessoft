cripto = {
    's': 'z',
    'a': 'e',
    'r': 'b',
    'b': 'r',
    'e': 'a',
    'z': 's'
    }

e = r'C:\Users\pedro\OneDrive\Documentos\GitHub\Dessoft\Exercicios\10.Arquivo\arquivos\06.criptografado.txt'
with open(e, 'r') as arquivo:
    conteudo = arquivo.read()

texto = ''
for c in conteudo:
    if c in cripto:
        texto += cripto[c]
    else:
        texto += c

print(texto)
