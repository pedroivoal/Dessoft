def quantos_uns(num):
    
    i = num
    d = 10
    r = 0

    while i != 0:

        c = i%d

        if c == 1:
            r += 1

        i = (i-c)/10

    return r

print(quantos_uns(123123))

# SOLUÇÃO COM LISTA(STRING)
# def quantos_uns(num):
#     snum = str(num)

#     r = 0
#     i = 0
#     while i < len(snum):

#         if snum[i] == '1':

#             r += 1
#         i += 1

#     return r