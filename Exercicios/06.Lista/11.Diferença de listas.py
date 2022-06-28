# l = [1,2,3,4,5,6,7,8]

# i = 0
# verificador = ''
# while i < len(l):
#     b = l.insert(i ,9)

#     if b != None:
#         verificador = 

def subtracao_de_listas(l_1, l_2):

    diferenca = []

    for i in l_1:
        if i not in l_2:
            diferenca.append(i)

    return diferenca
