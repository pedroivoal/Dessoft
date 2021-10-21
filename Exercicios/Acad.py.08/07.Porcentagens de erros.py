def calcula_porcentagens(dic):

    soma = 0
    for n_erros in dic.values():
        soma += n_erros

    for chave in dic:
        dic[chave] = dic[chave]/soma*100

    return dic

dice = {
    'Erro de indentação': 493,
    'Erro de parênteses': 1102,
    'Variável inexistente': 405,
}

print(calcula_porcentagens(dice))