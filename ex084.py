dados = list()
pessoas = list()
maior = menor = 0

while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso [Kg]: ')))

    if len(pessoas) == 0: #se eu não cadastrei ninguém ainda na lista pessoas
        maior = menor = dados[1] #dados[1] é o valor de peso
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    pessoas.append(dados[:])
    dados.clear()

    continuar = str(input('Quer continuar? [S/N]'))
    if continuar in 'Nn':
        break
print("*"*30)
print(f'O maior peso foi {maior}: ', end='')
for p in pessoas:
    if p[1] == maior:
        print(f'[{p[0]}]', end='')
print(f'\nO menor peso foi de {menor}',end='')
for p in pessoas:
    if p[1] == menor:
        print(f'[{p[0]}]',end='')
print(f'\nO total de pessoas cadastradas foram: {len(pessoas)}.')









