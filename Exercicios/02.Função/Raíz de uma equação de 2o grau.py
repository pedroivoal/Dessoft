def encontra_uma_raiz(a, b, c):

    Δ = b*b - 4*a*c
    R = (-b + Δ**(1/2))/(2*a)
    
    return R

# (x-3)(x+4) = x²+x-12 ⇒ a=1, b=1, c=-12
# PARA TESTAR FUNÇÃO
# print(encontra_uma_raiz(1,1,-12))
