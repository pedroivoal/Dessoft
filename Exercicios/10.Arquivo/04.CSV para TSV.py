e = r'C:\Users\pedro\OneDrive\Documentos\GitHub\Dessoft\Exercicios\10.Arquivo\04.dados.csv'
# dados.csv

tsv = ''
with open(e, 'r') as arquivo:

    conteudo = arquivo.read()

    for c in conteudo:

        if c == ',':
            tsv += '\t'
        else:
            tsv += c

e = r'C:\Users\pedro\OneDrive\Documentos\GitHub\Dessoft\Exercicios\10.Arquivo\04.dados.tsv'
with open(e, 'w') as arquivo:
    arquivo.write(tsv)
