def conta_bigramas(string):

    D_bigrams = {}
    i = 0
    while i < len(string)-1:

        bigram = string[i:i+2]
        n = string.count(bigram)
        D_bigrams[bigram] = n

        i += 1

    return D_bigrams

s = 'banana nanica'
print(conta_bigramas(s))