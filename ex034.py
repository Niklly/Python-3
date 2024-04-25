salario = float(input('Digite o valor do seu salário: R$'))

if salario <= 1250:
    novo = (salario * 0.15) + salario
    print('O salario de R${:.2f} passou a ser R${:.2f} agora.'.format(salario,novo))

else:
    novo = (salario * 0.10) + salario
    print('O salario de R${:.2f} passou a ser R${:.2f} agora.'.format(salario, novo))
