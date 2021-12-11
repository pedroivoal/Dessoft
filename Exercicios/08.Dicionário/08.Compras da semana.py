# 
def compras_da_semana(dic_de_pratos, lista_de_pratos):

    dic_de_compras = {}

    for prato in lista_de_pratos:
        for produto in dic_de_pratos[prato]:
            dic_de_compras[produto] = 0
            
    
    for prato in lista_de_pratos:        
        for produto in dic_de_pratos[prato]:
            dic_de_compras[produto] += dic_de_pratos[prato][produto]

    return dic_de_compras


# dic = {
#     'Bolo de chocolate': {
#         'Leite': 0.25,
#         'Óleo': 0.25,
#         'Ovo': 2.0,
#         'Farinha': 0.5,
#         'Açúcar': 0.2,
#         'Achocolatado': 0.3
#     },
#     'Bolinho de chuva': {
#         'Óleo': 1.0,
#         'Leite': 0.3,
#         'Ovo': 3.0,
#         'Farinha': 0.6,
#         'Açúcar': 0.3
#     },
#     'Mingau': {
#         'Açúcar': 0.1,
#         'Maizena': 0.1,
#         'Leite': 0.25
#     }
# }

# lista = ['Bolinho de chuva', 'Bolo de chocolate', 'Bolinho de chuva']

# print(compras_da_semana(dic, lista))