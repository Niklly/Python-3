print('\033[7;38;40m{:*^30}\033[m'.format('É PRIMO OU NÃO É'))
n = int(input('Digite um número qualquer: '))
tot = 0
for c in range(1, n+1):
    if n % c ==0:
        print('\033[33m', end='')
        tot +=1
    else:
        print('\033[30m', end='')
    print('{}'.format(c), end=' ')

print('\n\033[38mEsse número foi divisivel {} vez(es).'.format(tot))
if tot == 2:
    print('Por isso ele \033[33mÉ PRIMO\033[m.')
else:
    print('Por isso NÃO é PRIMO.')


