def divisivel(number):
    t1 = number % 2
    t2 = number % 3
    if (t1==0 and t2==0):
        return 'Insper'
    elif t1==0:
        return 'Ins'
    elif t2==0:
        return 'per'
    else:
        return number
