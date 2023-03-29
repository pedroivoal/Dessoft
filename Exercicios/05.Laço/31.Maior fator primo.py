import time

# def maior_fator_primo(n):
#     i = 2
#     while n != 1:
#         while n % i == 0:
#             n = n / i
#         i += 1
#     return i - 1

def maior_fator_primo(n):
    while n % 2 == 0:
        n = n / 2

    if n == 1:
        return 2
    
    i = 3
    while n != 1:
        while n % i == 0:
            n = n / i
        i += 2
    return i - 2

t0 = time.time()
print(maior_fator_primo(5*7*67*827*4040669))
tf = time.time()
print(f'Tempo para achar maior fator primo: {(tf-t0)*1000:.2f} ms')
# print(5*7*67*827*4040669)
# print(maior_fator_primo(7836130001735))