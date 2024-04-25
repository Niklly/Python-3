''' Crie um programa que tenha uma tupla única com nomes de produtos e
seus respectivos preços, na sequência.
No final, mostre uma listagem de preços,
organizando os dados em forma tabular.
'''
print('-'*41)
print('{:^41}'.format('LISTAGEM PREÇOS THZ'))
print('-'*41)

produtos = ('carregador universal',89.90,
            'mouse USB',125.50,
            'Iphone 14',2500.00)

for pos in range(0,len(produtos)):
    if pos % 2 == 0:
        print(f'{produtos[pos]:.<30}',end ='') #aqui ele vai pegar as posições pares
    else:
        print(f'R${produtos[pos]:>8.2f}') #aqui vai pegar as posições ímpares

print('-'*30)
