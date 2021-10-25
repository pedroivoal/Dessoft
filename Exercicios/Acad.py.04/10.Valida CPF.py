# 
def valida_cpf(n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11):

    #calcula valor do 1° verificador
    soma1 = n1*10 +  n2*9 + n3*8 + n4*7 + n5*6 + n6*5 + n7*4 + n8*3 + n9*2
    v1 = (soma1*10%11)%10

    #calcula valor do 2° verificador
    soma2 = n1*11 +  n2*10 + n3*9 + n4*8 + n5*7 + n6*6 + n7*5 + n8*4 + n9*3 + n10*2
    v2 = (soma2*10%11)%10

    if n1==n2 and n2==n3 and n3==n4 and n4==n5 and n5==n6 and n6==n7 and n7==n8 and n8==n9 and n9==n10 and n10==n11:
        return False
    elif v1 == n10 and v2 == n11:
        return True
    else:
        return False
