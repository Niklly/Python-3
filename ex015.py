km = float(input('Qual foi a quantidade de km percorridos? '))
d = int(input('Por quantos dias você alugou o carro? '))
preço_dia = 60 * d
preço_km = 0.15 * km

total = preço_km + preço_dia
print('O valor total a pagar será R${:.2f}'.format(total))



