# 
v = float(input())

if v > 80:
    mult = (v - 80)*5
    print('{:.2f}'.format(mult))
else:
    print('Não foi multado')