
def entregador_mais_proximo(restaurante, l_entregadores):
    
    xr = restaurante[0]
    yr = restaurante[1]

    xe = l_entregadores[0][0] 
    ye = l_entregadores[0][1] 

    distancia_min = ((xr-xe)**2 + (yr-ye)**2)**(1/2)
    i = 0

    for entregador in l_entregadores:

        xe = entregador[0] 
        ye = entregador[1] 

        distancia = ((xr-xe)**2 + (yr-ye)**2)**(1/2)

        if distancia < distancia_min:
            distancia_min = distancia
            i = l_entregadores.index(entregador)

    return i