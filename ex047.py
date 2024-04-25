print('\033[7;30;47m{:^30}\033[m'.format('NÚMEROS PARES'))

for c in range(1,51):
    if c % 2 == 0:
        print(c, end=' ') # o end = ' ' faz com que o resultado fique tudo na mesma linha. Assim evita espaço desnecessário no console.
print('FIM')


''' poderia ter feito esse código sem pensar em conta/resto da divisão
for c in range(2,51,2):    ou seja a partir do 2 pulando de 2 em dois(ou seja PAR)
    print(c, end=' ')
print('ACABOU')

Nesse código eu uso menos interação/menos trabalho para o meu computador pensar pois não terei que pensar de 1 em 1. Aqui eu faço metade, ou seja 25 números.
'''

