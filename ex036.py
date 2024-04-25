print('\033[38m-=-\033[m'*16)
print('\033[7;38;40m '*16,'BANCO THOMAZZI',' ' *16,' \033[m')

casa = float(input('Qual o valor(R$) da casa que você deseja comprar: \033[34mR$\033[m'))
salario = float(input('Quanto você ganha atualmente? \033[34mR$\033[m'))
tempo = int(input('Em quantos anos você quer pagar seu imóvel? '))

prestacao = casa / (tempo * 12)
requisito = salario * 0.3
print('-=-'*17)
if prestacao > requisito:
    print('\033[31mSinto informar mas seu empréstimo foi negado.\nO valor da prestação será R${:.2f}, e excede os 30% do seu salário.\033[m'.format(prestacao))

elif prestacao <= requisito:
    print('\033[34mPARABÉNS!! Seu empréstimo foi aceito.\033[m')
    print('\033[34mVocê terá que me pagar R${:.2f} por mês\033[m'.format(prestacao))

