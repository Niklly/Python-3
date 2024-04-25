distancia = float(input('Qual a distância da sua viagem? '))

if distancia <= 200:
    passagem = 0.5 * distancia
    print('Você está prestes a começar uma viagem de {}Km'.format(distancia))
    print('O valor da sua passagem será de R${:.2f}'.format(passagem))

else:
    passagem = 0.45 * distancia
    print('Você está prestes a começar uma viagem de {}Km'.format(distancia))
    print('O valor da sua passagem será de R${:.2f}'.format(passagem))
