numeros = list()

while True:
    n = int(input('Digite um valor: '))

    if n not in numeros:
        numeros.append(n)
        print('Número adicionado com sucesso :)')
    else:
        print('Esse número é duplicado!!')
    r = str(input('Quer continuar? [S/N]'))
    if r in 'Nn':
        break

numeros.sort()
print('='*30)
print(f'Esse números que você digitou:{numeros}')

