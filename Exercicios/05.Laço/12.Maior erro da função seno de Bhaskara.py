from math import sin, radians
dif = 0

x = 1
while x < 91:
    bsenx = (4*x*(180-x))/(40500-x*(180-x))

    senx = sin(radians(x))

    bdif = abs(senx-bsenx)

    if bdif > dif:
        r = x
        dif = bdif
    
    x += 1

print(r)
