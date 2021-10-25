# 
def nota_final(q, ai, af, ep1, ep2, pf):


    if q not in range(0, 10) or ai not in range(0, 10) or af not in range(0, 10) or ep1 not in range(0, 10) or ep2 not in range(0, 10) or pf not in range(0, 10):
        nf = 0

    else:

        ni = 0.4*ai + 0.5*af + 0.1*q

        ng = 0.1*ep1 + 0.2*ep2 + 0.7*pf

        if ni < 5 or ng < 5:
            nf = min(ni, ng)
        else:
            nf = (ni + ng)/2

    return nf