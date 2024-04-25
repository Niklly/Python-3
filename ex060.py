num = int(input('Digite um número para descobrir o seu fatorial:  '))

resultado = 1
contador = 1
while contador <= num:
    resultado = resultado * contador  #a cada resultado eu multiplico com um novo contador(até chegar no meu número).
    contador = contador + 1 #aqui eu vou de 1 até o meu número escolhido para fatora-ló
print('Fatorial de {}! {}'.format(num,resultado))



