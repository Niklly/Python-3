from random import randint
from time import sleep

lista = []
jogos = [] #lista com todos os jogos
tot = 1

quantidade = int(input('Digite a quantidade de jogos que queria sortear: '))
while tot <= quantidade: #quantidade de listas que vou gerar
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    lista.sort()
    jogos.append(lista[:]) #fiz uma copia dos numeros da lista para -> jogos
    lista.clear()
    tot += 1
print(f'-='*4,f'SORTEANDO {quantidade} JOGOS','=-'*4)
sleep(1)
for i, l in enumerate(jogos):
    print(f'Jogo{i+1}: {l}')
    sleep(1)
print('--------- BOA SORTE :) --------- ')

