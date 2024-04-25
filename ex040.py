print('\033[1;38;40m*\033[m' * 31)
print('\033[7;48m '*5, 'AVALIAÇÃO DE NOTAS', ' ' * 5, '\033[m')
print('\033[1;38;40m*\033[m' * 31)

nota_a = float(input('Digite a primeira nota: '))
nota_b = float(input('Digite a segunda nota: '))

media = (nota_a + nota_b)/2

if media < 5.0:
    print('\033[1;31mREPROVADO: sem possibilidade de prova.\033[m')

elif 6.9 >= media >= 5.0:
    print('\033[1;33mRECUPERAÇÃO: possibilidade de prova.\033[m')

else:
    print('\033[1;34mAPROVADO: passou direto.\033[m')

