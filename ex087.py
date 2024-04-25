matriz = [[0,0,0,], [0,0,0,], [0,0,0,]]
maior = soma = terceira = 0
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Dgite um valor para [{l}, {c}]: '))

print('-='*25)

for l in range(0,3):
    for c in range(0,3):
        print(f'\033[7;38;40m[{matriz[l][c]:^3}]\033[m', end='')
        if matriz[1][0] == 0:
            maior = matriz[0][0]
        elif matriz[1][c] > maior:
            maior = matriz[1][c]
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
    terceira += matriz[l][2]
    print()


print("-="*25)
print(f'\033[33mA soma dos valores pares é {soma}\033[m')
print(f'\033[33mA soma dos valores da terceira coluna é {terceira}\033[m')
print(f'\033[33mO maior valor da segunda linha é {maior}\033[m')
