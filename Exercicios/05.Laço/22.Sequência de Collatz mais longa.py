def sequence_length(n):

    i = 0
    while n != 1:
            
        if n%2 == 0:
            n /= 2
        else:
            n = 3*n + 1
        i += 1
    
    return i

i_bigger = 0
bigger = 0
i = 2
while i < 1000:

    length = sequence_length(i)

    if length > bigger:
        bigger = length
        i_bigger = i

    i += 1

print(i_bigger)