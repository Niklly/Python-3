import random

print('*-'*20)
print('\033[34;40m '*12, '-JOGO JOKENPÔ-', ' '*13,'\033[m')
print('*-'*20)

opcoes = ['tesoura', 'pedra', 'papel']
computador = random.choice(opcoes)

print('''Suas opções:
[ 0 ] TESOURA
[ 1 ] PEDRA
[ 2 ] PAPEL ''')

jogador = int(input('Qual será a sua jogada? '))
print('-='*15)
print('O computador jogou: {}'.format(computador))
print('Você jogou: {}'.format(opcoes[jogador]))
print('-='*15)

print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ')
print('...')
sleep(1)

'''computador ganha'''
if computador == 'tesoura' and jogador == 2:    #jogador joga papel
    print('EU VENCI')

elif computador == 'pedra' and jogador == 0:    #jogador joga tesoura
    print('EU VENCI')

elif computador == 'papel' and jogador == 1:    #jogador joga pedra
    print('EU VENCI')

elif jogador == 0 and computador == 'papel':    #jogador joga tesoura
    print('PARABÉNS!! VOCÊ GANHOU!')

elif jogador == 2 and computador == 'pedra':     #jogador joga papel
    print('[34mPARABÉNS!! VOCÊ GANHOU!')

elif jogador == 1 and computador == 'tesoura':     #jogador joga pedra
    print('PARABÉNS!! VOCÊ GANHOU!')

else:
    print('EMPATE! HAHA :)')