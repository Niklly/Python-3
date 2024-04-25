print('-'*30)
print('\033[7;36m{:^30}\033[m'.format('LOJA PREÇO BAIXO'))
print('-'*30)
menor = contador = total = totmil = 0
continuar = ' '
barato = ' '
while continuar != 'N':
    produto = str(input('Nome do produto: '))
    preço = float(input('Preço: R$'))
    contador += 1
    continuar = str(input('Quer continuar [S/N]: ')).strip().upper()

    total += preço

    if contador == 1 or preço < menor:
        menor = preço
        barato = produto
    if preço > 1000:
        totmil += 1
    if continuar == 'N':
        break
print('\033[31m{:-^30}\033[m'.format('CARRINHO/COMPRAS'))
print(f'O total da compra: {total:.2f}')
print(f'O total de produtos acima de R$1000,00: {totmil}')
print(f'O {barato} teve o menor preço: R${menor:.2f}')



