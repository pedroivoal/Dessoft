dic = {"Fulano":"99999-1111", "Sicrano":"99999-2222", "Beltrano":"99999-3333"}
nome_selecionado = input("Digite um nome: ").title()

print("Telefone de {0} é: {1}".format(nome_selecionado, dic[nome_selecionado]))