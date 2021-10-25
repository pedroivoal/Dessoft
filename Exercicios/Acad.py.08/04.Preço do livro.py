# 
def verifica_preco (titulo,dic_nome_cor,dic_cor_prec):

    cor = dic_nome_cor[titulo]
    prec = dic_cor_prec[cor]

    return prec


dicionário_de_livros = {'Pinóquio':'azul', "Dom Quixote": "amarelo", "O Pequeno Príncipe": "vermelho"}
cores  = {'vermelho': 10.0, 'azul': 20.0, 'amarelo': 40.0, "verde": 100.0 }

print(verifica_preco('Pinóquio', dicionário_de_livros, cores))