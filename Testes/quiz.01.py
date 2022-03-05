def calcula_segredo(num):
    if num<100:
        return -1
    elif num > 999:
        return -1
    else:
        u = num%10
        d = (num-u)%100/10
        c = (num-u-d*10)%1000/100
        r = u+c+d
        return r

# num = 729
# print(calcula_segredo(num))