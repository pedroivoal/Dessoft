def calcula_serie(a, b, n):
    Sum = 0
    for i in range(0,n):
        Sum += 1/a**(i*b)
    
    return Sum