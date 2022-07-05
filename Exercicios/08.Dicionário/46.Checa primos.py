def verifica_primos(L_numb):
    D_primes = {}

    for num in L_numb:

            c = 0
            z = int(num//2// +1)#acha o maior valor(sem conta o próprio número) que dividiria o número caso ele não fosse primo.
            if num == 1 or num == -1:
                c += 1
            elif 0 == num % 2 and num != 2:
                c += 1
            else:
                for i in range(3, z, 2):
                    if num%i == 0:
                        c += 1
            
            if c == 0:
                D_primes[num] = True
            else:
                D_primes[num] = False

    return D_primes

# L_n = [-1,0,1,2,3,4,5,6,7,8,9]
# print(verifica_primos(L_n))
