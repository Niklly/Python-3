'''
 Crie um programa onde o usuário possa digitar cinco valores numéricos e
 cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
 No final, mostre a lista ordenada na tela.
'''

numeros = []

for c in range(0,5):
    valor = int(input('Digite um valor: '))
    if (c == 0) or (valor > numeros[-1]): #se o número digitado for maior que o número que está na última posição
        numeros.append(valor)
        print('Número adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(numeros): #enquanto a posição for menor que o tamanho da lista
            if valor <= numeros[pos]:  #se o valor digitado for menor igual ao numero que está na posição (0,1,2,3,4)
                numeros.insert(pos, valor) #eu vou inserir o valor digitado na posição em que fiz a verificação que ele é menor que o número que estava antes
                print(f'O valor foi digitado na posição {pos}.')
                break
            pos += 1

print(f'Números digitados em ordem: {numeros}')




