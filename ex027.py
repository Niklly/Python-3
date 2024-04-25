nome = str(input('Digite seu nome completo: ')).title().strip()
dividir = nome.split()
ultimo = len(dividir)-1
print('Muito prazer em te conhecer {}!'.format(dividir[0]))
print('Seu primeiro nome é: {}'.format(dividir[0]))
print('Seu último nome é: {}'.format(dividir[ultimo]))
