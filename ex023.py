num = int(input('Escolha um número qualquer entre 0 e 9999: '))
#dividido = num.replace('', ' ')

#nesse caso, eu vou dividir o numero por tal e com esse numero eu vou pegar o resto da divisão por 10

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando seu numero {}'.format(num))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))
