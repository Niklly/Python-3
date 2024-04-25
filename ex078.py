lista = []
maior = menor = 0
for cont in range(0,5):
    lista.append(int(input(f'Digite um valor para a posição {cont}: ')))
    if cont == 0 or lista[cont] <= menor:
        menor = lista[cont]
    elif cont == 0 or lista[cont] >= maior:
        maior = lista[cont]
print(f'Você digitou os valores: {lista}')
print(f'O maior valor é \033[33m{maior}\33[m e se encontra na(s) posição(s)..',end='')
for posicao, v in enumerate(lista):
    if v == maior:
        print(f'{posicao}..',end='')
print(f'\nO menor valor é \033[33m{menor}\033[m e se encontra na(s) posição(s)..',end='')
for posicao, v in enumerate(lista):
    if v == menor:
        print(f'{posicao}..',end='')






