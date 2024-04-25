print('\033[31;40m{:^25}\033[m'.format('PROGRESSÃO ARITMÉTICA'))

n = int(input('Qual o primeiro termo da PA: '))
r = int(input('Qual a razão da PA: '))
print('{} ->'.format(n), end=' ')

for c in range(2,11):
    g = n + ((c-1)*r)
    print('{} -> '.format(g), end=' ')
print('ACABOU')

''' outra forma de calcular décimo termo de uma PA
n = int(input('digite o primeiro termo:'))
r = int(input('digite a razao:'))

decimo = n + (10-1) * razao
for c in range(primeiro, decimo + razao, razao):
    print('{}'.format(c), end='-> ')
print('ACABOU')


'''