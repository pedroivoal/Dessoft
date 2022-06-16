def maximo_divisor_comum(n1, n2):

    i = min(n1, n2)

    while i > 0:
        r1 = n1%i
        r2 = n2%i
        
        if r1==0 and r2==0:
            res = i
            break
        
        i -= 1
    
    return res

print(maximo_divisor_comum(13,923))