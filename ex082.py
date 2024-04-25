lista = []
pares = []
impares = []
while True:
    lista.append(int(input('Digite um valor: ')))
    continuar = str(input('Você quer continuar? [N/S]')).strip().upper()

    if continuar == 'N':
        break

for num in lista:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f'A lista completa é {lista}')
print(f'A lista com números pares: {pares}')
print(f'A lista com números ímpares: {impares}')

