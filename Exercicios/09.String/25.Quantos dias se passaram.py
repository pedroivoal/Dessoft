def dias_do_ano(data):

    n_dias = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    mes = int(data[3:5])
    dia = int(data[0:2])

    dias = sum(n_dias[:mes-1])+dia-1
    
    return dias

print(dias_do_ano('31/12/2021'))