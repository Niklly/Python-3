numeros = (int(input('Digite um número: ')),
           int(input('Digite um número: ')),
           int(input('Digite um número: ')),
           int(input('Digite um número: ')))
print(f'Você digitou os números: {numeros}')
print(f'O número 9 foi digitado {numeros.count(9)} vezes')

if 3 in numeros:
    print(f'O número 3 se encontra na {numeros.index(3)+1}° posição')
else:
    print('Não foi digitado o número 3 em nenhuma posição.')

print('Os números pares são: ',end='')
for par in numeros:
    if par % 2 == 0:
        print(par,end=' ')

