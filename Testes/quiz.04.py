def valor_a_devolver(prateleira, caixa, compras):
    valor = 0
    for g_produto in compras:

        pp = prateleira[g_produto[0]][g_produto[1]]
        pc = caixa[g_produto[0]][g_produto[1]]

        if pp < pc:

            valor += (pc-pp)*g_produto[2]
    return valor

# prateleira = {
#     'requeijão': {
#         'Minas': 5,
#         'Buritis': 6,
#         'Queijinho': 7 
#     },
#     'sabão': {
#         'Pura Espuma': 10,
#         'Lavagem Perfeita': 12.5,
#         'Cromo': 15.7
#     },
#     'arroz': {
#         'Prato Fundo': 20,
#         'Tio José': 23,
#         'Cadez': 25
#     },
#     'macarrão': {
#         'Sandra': 2,
#         'Massa Nobre': 4,
#         'Urbano': 5.3
#     }
# }
# caixa = {
#     'requeijão': {
#         'Minas': 5,
#         'Buritis': 7,
#         'Queijinho': 7 
#     },
#     'sabão': {
#         'Pura Espuma': 10.5,
#         'Lavagem Perfeita': 12.8,
#         'Cromo': 15.7
#     },
#     'arroz': {
#         'Prato Fundo': 20,
#         'Tio José': 23,
#         'Cadez': 26
#     },
#     'macarrão': {
#         'Sandra': 2,
#         'Massa Nobre': 4.5,
#         'Urbano': 5.3
#     }
# }
# compras = [
#     ['arroz','Prato Fundo',1],
#     ['requeijão','Buritis',2],
#     ['requeijão','Queijinho',1],
#     ['sabão','Pura Espuma',3]
# ]

# print(valor_a_devolver(prateleira, caixa, compras))