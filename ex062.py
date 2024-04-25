primeiro = int(input('Digite o primeiro valor da PA: '))
razao = int(input('Digite a razao da PA: '))

contador = 1

while contador <=10:
    resultado = primeiro + ((contador-1) * razao)
    contador +=1
    print('{}->'.format(resultado), end='')

n_esimo = int(input('\n[0]: finalizar o programa\n[n]: para saber mais termos\n\033[34mDIGITE:\033[m'))
while contador <= (n_esimo+10):
    resultado = primeiro + ((contador-1) * razao)
    contador +=1
    print('{}->'.format(resultado), end='')
    if n_esimo == 0:
        print('ACABOU O PROGRAMA.')
print('FIM')


