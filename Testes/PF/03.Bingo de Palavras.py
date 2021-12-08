def verifica_ganhador(text, D_players):
    # Configura texto para ser analisado
    text = text.lower()
    text = text.split()

    D_return = {}

    for k in D_players:
        D_return[k] = 0

        # Lê cada palavra chutada por cada jogador
        for p in D_players[k]:
            points = 0
            points += text.count(p + ',')
            points += text.count(p + '.')
            points += text.count(p + ':')
            points += text.count(p + ';')
            points += text.count(p)
            D_return[k] += points
    
    return D_return

string = '''Algum tempo hesitei se devia abrir estas memórias pelo princípio ou pelo fim, isto é, 
se poria em primeiro lugar o meu nascimento ou a minha morte. Suposto o uso vulgar seja começar pelo 
nascimento, duas considerações me levaram a adotar diferente método: a primeira é que eu não sou propriamente 
um autor defunto, mas um defunto autor, para quem a campa foi outro berço; a segunda é que o escrito ficaria 
assim mais galante e mais novo. Moysés, que tambem contou a sua morte, não a poz no introito, mas no cabo: 
diferença radical entre este livro e o Pentateuco.'''
D = {
    'joao': ['paz', 'memórias', 'fim'],
    'maria': ['defunto', 'livro', 'felicidade']
}

print(verifica_ganhador(string, D))