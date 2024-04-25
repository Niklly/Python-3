n1 = int(input('Digite o 1° valor: '))
n2 = int(input('Digite o 2° valor: '))

menu = 0
continuar = 'S'
maior = menor = 0

print('[1] - SOMAR')
print('[2] - MULTIPLICAR')
print('[3] - MAIOR')
print('[4] - NOVOS NÚMEROS')
print('[5] - SAIR DO PROGRAMA')

while continuar == 'S' and menu < 5:
    menu = int(input('Escolha uma opção: '))
    if menu == 1:
        print('A soma entre os números é {}'.format(n1+n2))
        continuar = str(input('Quer continuar [S/N]? ')).upper()

    elif menu == 2:
        print('A multiplicação entre os números é {}'.format(n1*n2))
        continuar = str(input('Quer continuar [S/N]? ')).upper()

    elif menu == 3:
        if n1 > n2:
            maior = n1
            print('O maior número é {}'.format(maior))
        elif n2 > n1:
            maior = n2
            print('O maior número é {}'.format(maior))
        else:
            print('Não exite maior, pois são iguais.')
        continuar = str(input('Quer continuar [S/N]? ')).upper()

    elif menu == 4:
        print('Tente novamente')
        n1 = int(input('Digite o 1° valor: '))
        n2 = int(input('Digite o 2° valor: '))

print('ACABOU')

