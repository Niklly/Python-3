from random import randint
print('\033[35;40m{:-^30}\033[m'.format('-VAMOS JOGAR PAR OU ÍMPAR?-'))
cont = 0
while True:
    computador = randint(0, 10)
    num_jogador = int(input('Digite um valor: '))
    jogador = str(input(('Par ou Ímpar? [P/I] '))).strip()
    soma = computador + num_jogador
    if soma % 2 == 0 and jogador in 'Ii':
        print(f'\033[7;30;45mVocê jogou {num_jogador} e o computador {computador}, total {soma} \033[m')
        print('\033[7;30;45m{:-^39}\033[m'.format('GAMER OVER'))
        break
    elif soma % 2 != 0 and jogador in 'Pp':
        print(f'\033[7;30;45mVocê jogou {num_jogador} e o computador {computador}, total {soma} \033[m')
        print('\033[7;30;45m{:-^39}\033[m'.format('GAMER OVER'))
        break
    elif soma % 2 == 0:
        if jogador in 'pP':
            cont += 1
            print('_'*35)
            print(f'Você jogou {num_jogador} e o computador {computador}, total {soma}')
            print('\033[35mVocê ganhou..\033[m Vamos jogar de novo?')
            print('_' * 35)
    elif soma % 2 != 0:
        if jogador in 'Ii':
            cont +=1
            print('_' * 35)
            print(f'Você jogou {num_jogador} e o computador {computador}, total {soma}')
            print('\033[35mVocê ganhou..\033[m Vamos jogar de novo?')
            print('_' * 35)
print(f'Você ganhou {cont} vez(es)')

# uma forma de fazer com que a  while não aceite a resposta errada, apenas as opções dadas:
# tipo = ' '
# while tipo not in 'PI':
#      tipo = str(input('PAR OU ÍMPAR:')).strip().upper()[0]