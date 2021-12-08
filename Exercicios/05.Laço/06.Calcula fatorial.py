def fatorial(n):
    r = 1

    i = 1
    while i <= n:

        r *= i
        i += 1

    return r

'''código que escreve as multiplicações de um fatorial'''
# def fatorial(n):
#     factorial = ''

#     i = 1
#     if n > 0:
#         factorial += '{}'.format(i)

#     i = 2
#     while i <= n:
#         factorial += ' . {}'.format(i)
#         i += 1

#     r = '{}! = {}'.format(n, factorial)

#     return r

# print(fatorial(20))