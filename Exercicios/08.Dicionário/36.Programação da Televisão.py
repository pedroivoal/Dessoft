def quando_passa(grade, programa0):

    D_programa = {}

    for canal, horarios in grade.items():

        for horario, programa in horarios.items():

            if programa == programa0:

                if horario in D_programa:
                    D_programa[horario].append(canal)
                else:
                    D_programa[horario] = [canal]

    return D_programa

d = {
    'Raposa TV': {
        '00h00': 'ModSim: Tudo é Possível',
        '01h00': 'Férias em Mathland',
        '07h00': 'Hora do Relaxamento',
        '15h00': 'Vale a Pena Rever a Matéria',
        '23h30': 'DesSoft: Hacking the Server'
    },
    'INN': {
        '08h00': 'Notícias do Campus',
        '10h00': 'Futuro: Intercâmbio',
        '12h00': 'Tele curso: Cálculo IV',
        '16h00': 'Os Mistérios de DesSoft',
        '20h00': 'Vale a Pena Rever a Matéria',
        '22h00': 'Culinária dos Salgados'
    },
    'Rede Insper TV': {
        '07h00': 'Hora do Relaxamento',
        '13h00': 'Campus em Foco',
        '16h00': 'Os Mistérios de DesSoft',
        '20h00': 'Hora do Relaxamento',
        '21h00': 'Futuro: Intercâmbio'
    }
}

print(quando_passa(d, 'Hora do Relaxamento'))
