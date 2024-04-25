print('\033[7;35;40m --Seja bem-vindo ao banco THZ-- \033[m')
while True:
    print('-' * 30)
    valor = int(input('Qual valor a ser sacado? R$'))
    print('-'*30)
    notacinquenta = valor // 50
    restocinquenta = valor % 50
    notavinte = valor // 20
    restovinte = valor % 20
    notadez = valor // 10
    restodez = valor % 10
    if valor == 0:
        break

    elif valor >= 50:
        print(f'Total de notas de R$50 = {notacinquenta}')
        if restocinquenta >= 20:
            notasdevinte = restocinquenta // 20
            restonotadevinte = restocinquenta % 20
            print(f'Total de notas de R$20 = {notasdevinte}')
            if restonotadevinte >= 10:
                resto = restonotadevinte - 10
                print('Total de notas de R$10 = 1')
                print(f'Total de notas de R$1 = {resto}')
            elif restonotadevinte >= 1:
                print(f'Total de notas de R$1 = {restonotadevinte}')
        elif restocinquenta >= 10:
            quant_um = restocinquenta - 10
            print('Total de notas de R$10 = 1')
            print(f'Total de notas de R$1 = {quant_um}')
        elif restocinquenta >= 1:
            print(f'Total de notas de R$1 = {restocinquenta}')

    elif 49 >= valor >= 20:
        print(f'Total de notas de R$20 = {notavinte}')
        if restovinte >= 10:
            sobra = restovinte - 10
            print(f'Total de notas de R$10 = 1')
            print(f'Total de notas de R$1 = {sobra}')
        if restovinte < 10:
            print(f'Total de notas de R$1 = {restovinte}')

    elif 19 >= valor >= 10:
        print(f'Total de notas de R$10 = {notadez}')
        if restodez != 0:
            print(f'Total de notas de R$1 = {restodez}')

    elif 9 >= valor >= 1:
        print(f'Total de notas de R$1 = {valor}')

print('\033[7;30;48mFINAL DA RETIRADA------------\033[m')
print('Agradecemos pela preferência!! \033[33m:)\033[m')



