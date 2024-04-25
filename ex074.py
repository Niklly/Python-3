''' Crie um programa que vai gerar 5 números aleátorios e colocar dentro de uma tupla

A) Mostre a listagem de números gerados
B) Indique o menor e o maior número que está dentro da tupla
'''
from random import randint

num = randint(1,10)
num2 = randint(1,10)
num3 = randint(1,10)
num4 = randint(1,10)
num5 = randint(1,10)

numeros = (num,num2,num3,num4,num5)
menor = maior = c = 0

for c in range(0,5):
    if c == 0 or numeros[c] <= menor:
        menor = numeros[c]
    if c == 0 or numeros[c] >= maior:
        maior = numeros[c]

print(f'Os números sorteados foram: {numeros}')
print('*'*20)
print(f'O menor é {menor}')
print(f'O maior é {maior}')





