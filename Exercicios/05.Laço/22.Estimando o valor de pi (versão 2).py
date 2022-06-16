def PiWallis(times):
    piw = 2
    n = 2
    d = 1

    i = 0
    while i in range(0, times):

        if i%2 == 0 and i != 0:
            n += 2
        elif i%2 == 1:
            d += 2

        piw *= n/d        
        i += 1

    return piw

print(PiWallis(1))