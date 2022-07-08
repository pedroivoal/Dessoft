from json import loads

e = r'C:\Users\pedro\OneDrive\Documentos\GitHub\Dessoft\Exercicios\10.Arquivo\arquivos\05.estoque.json'
# estoque.json
# \05.estoque.json
with open(e, 'r') as arquivo:
    texto = arquivo.read()

dic = loads(texto)

s = 0
for produto in dic['produtos']:
    s += float(produto['quantidade']) * float(produto['valor'])

print(s)
