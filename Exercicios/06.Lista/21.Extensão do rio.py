def calcula_extensao(x, y):

    d = 0
    i = 0
    while i < len(x)-1:
        d += ((x[i+1]-x[i])**2 + (y[i+1]-y[i])**2)**(1/2)
        i += 1
        
    return d

Coordenadasx = [275, 290, 310, 390, 480]
Coordenadasy = [75, 180, 120, 110, 150]

print(calcula_extensao(Coordenadasx, Coordenadasy))