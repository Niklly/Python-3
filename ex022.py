nome = str(input('Digite o seu nome completo: '))
#print(len(nome.replace(" ","")))
dividido = nome.split()

print('Seu nome em maiscúlo: {}'.format(nome.upper()))
print('Seu nome em minuscúlo: {}'.format(nome.lower()))
print('A quantidade de letras ao todo: {}'.format(len(nome.replace(" ",""))))
print('A quantidade de letras no 1° nome: {}'.format(len(dividido[0])))

# outra forma de eliminar os espaços:
# nome = str(input('Digite o seu nome completo: ')).strip()
# print('Seu nome tem o total de {} letras'.format(len(nome)- nome.count(' ')))

# outra forma de saber quantas letras tem o primeiro nome:
# print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))