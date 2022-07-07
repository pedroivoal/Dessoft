# Cria o arquivo para escrita (limpa o antigo se já existir)
with open(r'C:\Users\pedro\OneDrive\Documentos\GitHub\Dessoft\Handout\10.Arquivo\ex.txt', 'w') as arquivo:
    # Escrevendo um texto
    arquivo.write("algum dado\n")

# Abre/Cria o arquivo para escrita SEM apagar o que tinha antes.
with open(r'C:\Users\pedro\OneDrive\Documentos\GitHub\Dessoft\Handout\10.Arquivo\ex.txt', 'a') as arquivo:
    # Escrevendo um texto
    arquivo.write("novo dado\n")
