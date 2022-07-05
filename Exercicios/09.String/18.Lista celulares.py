def lista_celulares(l_contacts):
    l_phone_numbers = []
    for i in l_contacts:
        if len(i)==14:
            number = i[5:]
            l_phone_numbers.append(number)
        elif len(i)==11:
            number = i[2:]
            l_phone_numbers.append(number)
        elif len(i)==9:
            number = i
            l_phone_numbers.append(number)

    return l_phone_numbers
    