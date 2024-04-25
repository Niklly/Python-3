n = int(input('Digite um número para descobrir seu fatorial: '))

contador = n
resultado = 1
print('O fatorial de {}! = '.format(n), end='')
while contador > 0:
    print('{} '.format(contador), end='')
    print('x ' if contador > 1 else '=', end='')
    resultado = resultado * contador
    contador -= 1
print('{}'.format(resultado))

