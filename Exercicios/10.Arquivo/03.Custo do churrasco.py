e = r'C:\Users\pedro\OneDrive\Documentos\GitHub\Dessoft\Exercicios\10.Arquivo\churras.txt'
# churras.txt

with open(e, 'r') as arquivo:
    print(arquivo)
    linhas = arquivo.readlines()
    print(linhas)

custo = 0
for linha in linhas:
    infs  = linha.split(',')
    custo += float(infs[1])*float(infs[2])

print(custo)
