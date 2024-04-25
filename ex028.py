import random
from time import sleep

num = [0,1,2,3,4,5]  #criei uma lista os possíveis numeros a seres escolhidos
comp = random.choice(num) #o computador vai pensar entre 0 e 5

print('-'*55)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-'*55)

voce = int(input('Adivinhe o número que eu pensei?')) # aqui o jogador joga
print('PROCESSANDO...')
sleep(3)

if voce == comp:
    print('Parabéns!! Você adivinhou meu número')
else:
    print('Ganhei!! Eu pensei no número {} e não no {}'.format(comp,voce))

print('--FIM--')


#eu tambem posso  importar o random e utilizar a funçao randit(0,5) que irá gerar um número aleatorio entre 0 e 5.