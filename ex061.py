primeiro = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razao da PA: '))

contador = 1

while contador <= 10:
    resultado = primeiro + ((contador-1) * razao)
    contador +=1
    print('{}->'.format(resultado), end='')

print('FIM')



