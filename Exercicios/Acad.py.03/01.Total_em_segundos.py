# 
dia = int(input('Digite o número de dias: '))
hora = int(input('Digite o número de horas: '))
minuto = int(input('Digite o número de minutos: '))
s = int(input('Digite o número de segundos: '))

sd = dia*24*60*60
sh = hora*60*60
sm = minuto*60

r = sd + sh + sm + s

print (r)