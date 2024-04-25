print('*-' * 17)
print('\033[7;38m '*5,'COMPARAÇÃO DE NÚMEROS', ' '*5, '\033[m')

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))

if a > b:
    print('O \033[2;34mprimeiro\033[m número é maior.')

elif b > a:
    print('O \033[2;34msegundo\033[m número é maior.')

else:
    print('Não existe valor maior. Os dois \033[1;34msão iguais.\033[m')
