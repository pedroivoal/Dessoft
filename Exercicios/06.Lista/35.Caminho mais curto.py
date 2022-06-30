def calcula_caminho(coordenadas):

    d = 0
    i = 0
    while i < len(coordenadas)-1:
        d += ((coordenadas[i+1][0]-coordenadas[i][0])**2 + (coordenadas[i+1][1]-coordenadas[i][1])**2)**(1/2)
        i += 1

    return d

def caminho_mais_curto(caminhos):

    l_dist = []
    i = 0
    while i < len(caminhos):

        l_dist.append(calcula_caminho(caminhos[i]))
        i += 1
    
    i_do_menor = l_dist.index(min(l_dist))

    return caminhos[i_do_menor]


# caminhos = [[[5, 2], [3, 7], [7, 3], [10, 4]],[[5, 2], [300, 1000], [10, 4]]]

# caminhos = [[[5,2],[300,1000],[10,4]],[[5,2],[3,7],[7,3],[10,4]]]

caminhos = [[[32,61],[33,60],[100,50],[23,63],[102,57]],[[32,61],[102,57]],[[32,61],[20,60],[102,57]]]

print(caminho_mais_curto(caminhos))