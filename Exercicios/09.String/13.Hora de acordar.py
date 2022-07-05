def converteHora(horario):

    i = horario.find(':')
    hora = int(horario[0:i])
    minuto = horario[i+1:]

    if hora < 12:
        horario = f'{hora}:{minuto} AM'
    elif hora < 13:
        horario = f'{hora}:{minuto} PM'
    else:
        horario = f'{hora-12}:{minuto} PM'

    if len(horario) == 7:
        horario = '0' + horario
        
    return horario

print(converteHora('12:00'))
