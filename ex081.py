lista = []
while True:
    n = int(input("Digite um valor: "))
    lista.append((n))
    continuar = str(input('Quer continuar? [S/N]')).strip().upper()
    if continuar == 'N':
        break

lista.sort(reverse=True)
print(f'Você digitou {len(lista)} elementos.')
print(f'Os números digitados em ordem decrescente foram: {lista}')
if 5 in lista:
    print('O número 5 está na lista')
else:
    print('Não foi encontrado o número 5.')


