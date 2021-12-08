# 
def raiz_quadrada(num):

    if num == 0:
        sqrt_r  = 0
    else:
        imp = 1
        while 0 != num:
            num = num -imp
            imp += 2
            sqrt_r  = ((imp-1)/2)
        
    return  sqrt_r