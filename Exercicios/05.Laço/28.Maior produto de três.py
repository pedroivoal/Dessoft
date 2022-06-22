
def maior_produto3(l_num):

    menor1 = min(l_num)
    l_num.remove(menor1)
    menor2 = min(l_num)

    maior1 = max(l_num)
    l_num.remove(maior1)
    maior2 = max(l_num)
    l_num.remove(maior2)
    maior3 = max(l_num)

    bigger1 = menor1 * menor2 * maior1
    bigger2 = maior1 * maior2 * maior3

    if bigger1 < bigger2:
        return bigger2
    else:
        return bigger1