import math
num = int(input('Digite um número inteiro qualquer: '))
conversao = int(input('Você gostaria de convete-lo para qual base de conversão?\n1: binario\n2: octal\n3: hexadecimal\n'))

if conversao == 1:
    convertido = bin(num)
    print('\033[7;38mO valor de {} em binário é: {}\033[m'.format(num,convertido[2:]))

elif conversao == 2:
    convertido = oct(num)
    print('\033[7;38mO valor de {} em octal é: {}\033[m'.format(num,convertido[2:]))

elif conversao == 3:
    convertido = hex(num)
    print('\033[7;38mO valor de {} em hexadecimal é: {}\033[m'.format(num, convertido[2:]))

else:
    print('\033[7;38mO valor é inválido. Tente novamente.\033[m')

''' FORMAS DE PRINTAR AS OPÇÕES SEM TER QUE COLOCAR TUDO NO INPUT

print('Escolha uma das bases para conversão
[1] binario
[2] octal
[3] hexadecimal
'
num = int(input('escolha a sua opção: '))
'''