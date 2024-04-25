print('\033[1;33;40m{:-^30}\033[m'.format('AVALIANDO FRASES'))
print('\033[1;33;40m{:-^30}\033[m'.format('PALÍNDROMOS'))

frase = str(input('Digite uma frase: ')).strip().lower()
palavras = frase.split() #Aqui eu fiz uma lista com cada palavra separada
junto = ''.join(palavras) #Aqui eu juntei todas as palavras, como se fosse apenas uma
frase_invertida = junto[::-1] #aqui eu inverti a frase juntada

for c in range(1):
    if frase_invertida == junto:
        print('Temos um PALÍNDROMO.')
    else:
        print('NÃO É PALÍNDROMO.')
