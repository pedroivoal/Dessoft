e = r'C:\Users\pedro\OneDrive\Documentos\GitHub\Dessoft\Exercicios\10.Arquivo\arquivos\02.macacos-me-mordam.txt'
# macacos-me-mordam.txt

with open(e, 'r') as arquivo:

    conteudo = arquivo.read()

conteudoF = ''
simbolos =  '!"#$%&()*+,-./:;<=>?@[\]^_`{|}~' # exerto espaço
for c in conteudo:
    if c not in simbolos:
        conteudoF += c

palavras = conteudoF.lower().split()
cont = 0
for palavra in palavras:

    if palavra == 'banana':
        cont += 1

print(cont)
