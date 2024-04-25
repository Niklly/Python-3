numeros = []
for c in range(1,8):
    numeros.append(int(input(f'Digite {c}° número:')))
numeros.sort()
print('Os valores digitados pares foram: ',end='')

for par in numeros:
    if par % 2 == 0:
        print(f'[{par}]',end='')

print('\nOs valores ímpares digitados foram: ',end='')
for impar in numeros:
    if impar % 2 == 1:
        print(f'[{impar}]',end='')


