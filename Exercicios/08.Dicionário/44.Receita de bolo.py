def converte_receita(receita):

    medidas = {
        'xícara': 250,
        'xícaras': 250,
        'colher de sopa': 15,
        'colheres de sopa': 15,
        'colher de chá': 5,
        'colheres de chá': 5
    }
    receita_convertida = {}

    for ingrediente, quantia in receita.items():

        if len(quantia)==1:
            receita_convertida[ingrediente] = quantia
        else:
            n = int(quantia[0])
            medida = quantia[2:]
            valor = n*medidas[medida]
            receita_convertida[ingrediente] = str(valor)+' ml'

    return receita_convertida

receita = { "ovos":"4", "açúcar":"2 xícaras", "leite":"1 xícara", "farinha":"2 xícaras", "fermento": "1 colher de sopa","baunilha":"1 colher de chá" } 
print(converte_receita(receita))
# Saída_da_função = {'ovos': '4', 'açúcar': '500 ml', 'leite': '250 ml', 'farinha': '500 ml', 'fermento': '15 ml', 'baunilha': '5 ml'}
