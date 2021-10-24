def promocao_viagens(dic):

    dic_r = {}

    for place, list in dic.items():
        price = list[1]*(10-list[0])/10 #preço com desconto

        dic_r[place] = price

    return dic_r

destinos = {
    "Miami":[1,1000],
    "Ilhas Sandwich do Sul":[4,5000],
    "Barcelona":[2, 2000],
    "Antártica":[5,200],
    "Buenos Aires":[3,500]
    }

print(promocao_viagens(destinos))