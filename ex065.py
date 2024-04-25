continuar = 'S'
contador = 0
soma = 0
maior = menor = 0
while continuar == 'S':
    num = int(input(('Digite um valor: ')))
    continuar = str(input('Quer continuar [S/N]? ')).upper()
    contador +=1
    soma += num
    if contador == 1:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num

print('Foram digitados {} números e a média entre eles é: {}'.format(contador, soma/contador))
print('O menor número digitado foi {} e o maior número {}'.format(menor, maior))
