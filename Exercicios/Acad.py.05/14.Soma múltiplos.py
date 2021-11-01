def soma_multiplos(n1, n2):

    Sum = 0
    stop = max(n1, n2)*10
    mult1 = n1
    mult2 = n2

    while mult1 <= stop or mult2 <= stop:

        if mult1 < mult2: 
            Sum += mult1
            mult1 += n1
        elif mult1 > mult2:
            Sum += mult2
            mult2 += n2
        else:
            Sum += mult1
            mult1 += n1
            mult2 += n2

    return Sum

print(soma_multiplos(5,2))
