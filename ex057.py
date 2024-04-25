sexo = ''
sexo = str(input('Digite o seu sexo [F/M]: ')).upper()
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Dados inválidos. Digite o seu sexo [F/M]: ')).upper()
print('ACABOU')
