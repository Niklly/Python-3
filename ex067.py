print('----TABUADA INFINITA----')

while True:
    c = 0
    print('\033[38m=\033[m' * 25)
    n = int(input('Digite um valor: '))
    print('\033[38m=\033[m' * 25)
    if n < 0:
        print('\033[7;35;48m{:^25}\033[m'.format('FINAL DO PROGRAMA'))
        break
    while c < 10:
        c += 1
        print(f'{n} x {c} = {n * c}')


#posso fazer esse mesmo programa usando um = for c in range(1,11):