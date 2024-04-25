import random

numeros = [1,2,3,4,5,6,7,8,9,10]
computador = random.choice(numeros)

jogador = 0
tentativas = 0

while jogador != computador:
    jogador = int(input('Adivinhe o numero que eu pensei: '))
    tentativas += 1
print('\033[35mParabens!! Eu pensei no número {}\033[m.\nMas você precisou de \033[31m{}\033[m tentativas para ganhar.'.format(computador, tentativas))

