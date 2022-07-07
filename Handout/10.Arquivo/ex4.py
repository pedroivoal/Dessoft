e = r'C:\Users\pedro\OneDrive\Documentos\GitHub\Dessoft\Handout\10.Arquivo\cancao_do_exilio.txt'

def p1():
    # Lendo tudo de uma vez
    with open(e, 'r') as arquivo:
        conteudo_completo = arquivo.read()
    print(conteudo_completo)

def p2():
    # Lendo apenas a primeira linha
    with open(e, 'r') as arquivo:
        primeira_linha = arquivo.readline()
    print(primeira_linha)

def p3():
    # Lendo de linha em linha (note o plural em readlines)
    with open(e, 'r') as arquivo:
        # linhas é uma lista de strings, cada linha é uma string diferente
        linhas = arquivo.readlines()
        # Verificando que linhas é uma lista de strings
        print(linhas)
        # Imprimindo de linha em linha
        for linha in linhas:
            print(linha)


p1()
p2()
p3()
