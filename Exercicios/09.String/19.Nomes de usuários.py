def extrai_nomes_de_usuarios(emails):

    nomes = []
    for email in emails:

        i = email.find('@')
        nome = email[0:i]
        nomes.append(nome)

    return nomes
