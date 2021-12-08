# 
d = float(input('Digite a distância da viagem: '))
ex = d - 200
if ex > 0:
    pre = 100 + ex*0.45
else:
    pre = 0.5*d
print('{:.2f}'.format(pre))