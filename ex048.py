print('\033[7;30;47m{:^30}\033[m'.format('NÚMEROS ÍMPARES'))
t = 0
n = 0
for c in range(1, 501):
    if c % 2 == 1:
        if c % 3 == 0:
            t += c
            n += 1
print('A soma dos {} \033[1;30mnúmeros ímpares\033[m múltiplos de 3 é: {}'.format(n, t))


