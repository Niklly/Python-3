palavras = ('Nikelly','Naiara','Lucio')


for nome in palavras:
    print(f'\nNa palavra {nome} temos: ',end='')
    for letra in nome:
        vogais = 'aeiou'
        if letra in vogais:
            print(f'{letra}', end='')




