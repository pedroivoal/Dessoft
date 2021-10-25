def pais_campeao(dic):

    lista = ['', 0, 0, 0]

    for Cname, dic_m in dic.items():

        if (dic_m['ouro'] > lista[1]) or (dic_m['ouro'] == lista[1] and dic_m['prata'] > lista[2]) or (dic_m['ouro'] == lista[1] and dic_m['prata'] == lista[2] and dic_m['bronze'] > lista[3]):
            lista[0] = Cname
            lista[1] = dic_m['ouro']
            lista[2] = dic_m['prata']
            lista[3] = dic_m['bronze']
    
    return lista[0]


# dicB = {
#     'China': {
#         'ouro': 20,
#         'prata': 35,
#         'bronze': 40 
#     },
#     'Canadá': {
#         'ouro': 5,
#         'prata': 15,
#         'bronze': 20
#     },
#     'Estados Unidos': {
#         'ouro': 25,
#         'prata': 30,
#         'bronze': 40
#     },
#     'Brasil': {
#         'ouro': 10,
#         'prata': 10,
#         'bronze': 8
#     }
# }

# print(pais_campeao(dicB))