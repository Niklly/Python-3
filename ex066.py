print('-='*20)
cont = soma = 0
while True:
    n = int(input('Digite um número (999 para parar): '))
    if n == 999:
        break
    cont += 1
    soma += n
print('~'*30)
print(f'Foram digitados \033[33m{cont}\033[m números. \nA soma entre eles \033[33m{soma}\033[m.')

