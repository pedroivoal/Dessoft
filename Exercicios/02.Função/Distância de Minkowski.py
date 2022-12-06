def distancia(x1, y1, x2, y2, p):
    dx = abs(x1-x2)**p
    dy = abs(y1-y2)**p
    d = (dx+dy)**(1/p)

    return d
