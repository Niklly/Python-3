contador = 0
soma = 0
num = 0
while num != 999:
    num = int(input('Digite um número inteiro: '))
    if num != 999:
        contador += 1
        soma += num
print('Foram digitados {} números, e a soma entre eles é {}.'.format(contador, soma))
print('FIM')



