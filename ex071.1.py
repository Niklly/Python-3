print('='*30)
print('\033[7;38;45m{:^30}\033[m'.format('BANCO TOMAZZI'))
print('='*30)

dinheiro = int(input('Quanto você quer sacar: R$'))
total = dinheiro
céd = 100
contador_céd = 0
while True:
    if total >= céd:
        total -= céd
        contador_céd += 1
    else:
        if contador_céd >= 1:
            print(f'Total de notas de R${céd}: {contador_céd}')
        if céd == 100:
            céd = 50
        elif céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:

            céd = 1
        contador_céd = 0

        if total == 0:
            break