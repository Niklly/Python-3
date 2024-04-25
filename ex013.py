salario = float(input('Quanto você ganha hoje? R$'))

aumento = salario * 0.15
reajuste = salario + aumento
print('Parabéns! Você recebeu um aumento de 15%. Agora seu salário é R${:.2f}'.format(reajuste))
