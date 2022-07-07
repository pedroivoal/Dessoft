e = r'C:\Users\pedro\OneDrive\Documentos\GitHub\Dessoft\Exercicios\10.Arquivo\texto.txt'
simbolos =  ' !"#$%&()*+,-./:;<=>?@[\]^_`{|}~'

with open(e, 'r') as arquivo:

    conteudo = arquivo.read()
    palavras = conteudo.split()

print(len(palavras))
