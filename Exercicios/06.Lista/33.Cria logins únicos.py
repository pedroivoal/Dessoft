
def login_disponivel(login, l_logins):
    
    if login not in l_logins:
        return login

    i = 1
    while True:

        novo_login = login+str(i)
        if novo_login not in l_logins:
            return novo_login

        i += 1


login = ''
l_logins = []
login = input('')

while login != 'fim':

    l_logins.append(login_disponivel(login, l_logins))
    login = input('')

for login in l_logins:
    print(login)
