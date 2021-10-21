def eh_palindromo(palavra):
    
    if palavra == palavra[-1::-1]:
        return True
    else:
        return False

print(eh_palindromo('roma é amor'))