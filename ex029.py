velocidade = float(input('Qual é a velocidade atual do carro? '))
print('-=-'*17)
if velocidade <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    calculo = velocidade - 80
    multa = calculo * 7
    print('MULTADO! Você excedeu o limite permitido que é 80km/h.')
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
    print('Tenha um bom dia! Dirija com segurança!')