def mais_populoso(D_br):
    biger = 0

    for kbr in D_br:
        s = 0

        for ve in D_br[kbr].values():
            s += ve

        if s > biger:
            r = kbr
            biger = s

    return r

brasil = {
"São Paulo": {"São Paulo": 21571281, "Campinas": 3224443},
"Minas Gerais": {"Belo Horizonte": 2385639, "Uberlândia": 611903},
}

print(mais_populoso(brasil))