e = r'C:\Users\pedro\OneDrive\Documentos\GitHub\Dessoft\Exercicios\10.Arquivo\01.texto.txt'
simbolos =  ' !"#$%&()*+,-./:;<=>?@[\]^_`{|}~'

with open(e, 'r') as arquivo:

    conteudo = arquivo.read()
    palavras = conteudo.split()

print(len(palavras))
