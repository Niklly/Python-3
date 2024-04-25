expressao = []
n = input('Digite a expressão:')
expressao.append((n))

contaabre = n.count('(')
contafecha = n.count(')')

if contaabre != contafecha:
    print('A sua expressão está errada')
else:
    print('A sua expressão está correta.')
