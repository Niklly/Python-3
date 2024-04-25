''' Desenvolva um programa que leia 4 valores pelo teclado e guarde-os em uma tupla. No final, mostre:

a) quantas vezes o valor 9 apareceu
b) em que posição foi digitado o primeiro valor 3
c) quais foram os números pares

'''
num = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
num3 = int(input('Digite um número: '))
num4 = int(input('Digite um número: '))

numeros = (num,num2,num3,num4)


print(f'Você digitou: {numeros}')

if 9 in numeros:
    print(f'Foi digitado {numeros.count(9)} vezes o número 9.')
else:
    print('Não foi digitado nenhum 9.')
if 3 in numeros:
    print(f'O número 3 se encontra na {numeros.index(3)+1}° posição')
else:
    print('Não foi digitado nenhum 3.')


c = q = 0
par = False
for c in range(0,4):
    if numeros[c] % 2 == 0:
        q += 1
        par = True
        print(f'Par: {numeros[c]}')

    elif q == 0:
        print('Não temos números pares.')
        break


















