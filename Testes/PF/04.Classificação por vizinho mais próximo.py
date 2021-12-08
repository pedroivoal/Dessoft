def acha_distancia(x1, y1, x2, y2):
    d = ((x1-x2)**2 + (y1-y2)**2)**(0.5)
    return d

def classifica(D_fish, dim):
    menor = 1000
    x1 = dim[0]
    y1 = dim[1]

    for k in D_fish:
        size = len(D_fish[k])

        for i in range(0, size):
            x2 = D_fish[k][i][0]
            y2 = D_fish[k][i][1]
            d = acha_distancia(x1, y1, x2, y2)

            if d < menor:
                r = k
                menor = d

    return r

D = {
    'salmao': [[8, 6], [12, 5], [10, 4]],
    'robalo': [[9, 3], [8, 2], [7, 3]],
    'sardinha': [[1, 2], [2, 3], [2, 2]]
}

L = [10, 2]

print(classifica(D, L))