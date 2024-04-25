print('\033[1;38m#\033[m' * 40)
print('\033[7;38m '*17, 'CAIXA', 15 * ' ', '\033[m')
print('\033[1;38m#\033[m' * 40)


preco = float(input('Qual o valor do produto que deseja? \033[33mR$\033[m'))
print('''\033[40mFORMAS DE PAGAMENTO\033[m
[1]: A vista(dinheiro/cheque)
[2]: A vista(cartão)
[3]: Crédito(2x)
[4]: Crédito(3x ou mais)''')

pagamento = int(input('Escolha: '))

if pagamento == 1:
    desconto = preco * 0.1
    final = preco - desconto
    print('Você ganhou 10% de desconto. Valor final: \033[34mR${:.2f}\033[m'.format(final))

elif pagamento == 2:
    desconto = preco * 0.05
    final = preco - desconto
    print('Você ganhou 5% de desconto. Valor final: \033[34mR${:.2f}\033[m'.format(final))

elif pagamento == 3:
    print('Você não ganha desconto. Valor final: \033[34mR${}\033[m'.format(preco))

else:
    juros = preco * 0.2
    final = preco + juros
    print('Essa forma de pagamento possui juros de 20%. Valor final: \033[34mR${:.2f}\033[m'.format(final))

''' aqui eu vou aprender a centralizar deterinada frase em x espaços

print('{:=^40}'.format('LOJAS POPULAR))
resultado:
=========LOJAS POPULAR=========

'''