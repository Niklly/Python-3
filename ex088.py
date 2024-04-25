from random import randint
from time import sleep

print('\033[1;30m*\033[m'*30)
print('\033[1;38m------JOGO DA MEGA SENA-------\033[m')
print('\033[1;30m*\033[m'*30)

palpites = int(input('Quantos jogos você quer que eu sortei? '))
print(f'=-=-=- SORTEANDO {palpites} JOGOS -=-=-=')
sleep(2)
for c in range(1, palpites+1): #quantidade de jogos que vou querer
    lista = palpites * []
    for num in range(0,6):  # aqui estou sorteando 6 números e adicionando dentro da lista-> é um jogo
        numero = randint(1,60)
        if numero not in lista:
            lista.append(numero)
        else:
            numero = randint(1, 60)
            lista.append(numero)
    lista.sort()
    print(f'Jogo{c}: {lista}')
    sleep(2)

print('\033[7;38m-=-=-=-= < BOA SORTE!!! > =-=-=-=-\033[m')
