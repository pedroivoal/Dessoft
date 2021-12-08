def tem_estoque(D_car, D_picies):
    a = 0 
    for kc,vc in D_car.items():

        if kc in D_picies:

            if D_picies[kc]>= vc:
                a += 0
            else:
                a += 1
        else:
            a += 1
        
    if a == 0:
        return True
    else:
        return False

d1 = {
    'motor': 1,
    'porta esquerda': 1,
    'porta direita': 1,
    'roda': 3,
}

d2 = {
    'hélice': 149,
    'motor': 56,
    'porta esquerda': 100,
    'porta direita': 42,
    'roda': 1304,
    'turbina': 23,
}

print(tem_estoque(d1, d2))