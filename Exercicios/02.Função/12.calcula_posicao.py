def calcula_posicao(So, Vo, a, t):

    T2 = 0.5*a*t*t
    S = So + Vo*t + T2
    
    return S
