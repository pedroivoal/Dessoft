
pacients_n = 0
age = 0
A = 0
B = 0
C = 0
D = 0
E = 0
F = 0

while age >= 0:
    age = int(input())
    
    if age < 0:
        break

    pacients_n += 1

    if age < 12:
        A += 1
    elif age < 18:
        B += 1
    elif age < 26:
        C += 1
    elif age < 36:
        D += 1
    elif age < 60:
        E += 1
    else:
        F += 1


A1 = A*100/pacients_n
B1 = B*100/pacients_n
C1 = C*100/pacients_n
D1 = D*100/pacients_n
E1 = E*100/pacients_n
F1 = F*100/pacients_n

print('''
0-11 anos: {:.2f} %
12-17 anos: {:.2f} %
18-25 anos: {:.2f} %
26-35 anos: {:.2f} %
36-59 anos: {:.2f} %
Acima de 60 anos: {:.2f} %
'''.format(A1, B1, C1, D1, E1, F1))