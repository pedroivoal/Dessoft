# 
def nota_final(q, ai, af, ep1, ep2, pf):

    if 0<=q<=10 and 0<=ai<=10 and 0<=af<=10 and 0<=ep1<=10 and 0<=ep2<=10 and 0<=pf<=10:

        ni = 0.4*ai + 0.5*af + 0.1*q

        ng = 0.1*ep1 + 0.2*ep2 + 0.7*pf

        if ni < 5 or ng < 5:
            nf = min(ni, ng)
        else:
            nf = (ni + ng)/2

        return nf

    nf = 0
    return nf