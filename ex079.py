''' 1° Crie um programa onde o usuário possa digitar vários valores numéricos
2° cadastre-os em uma lista.
3° Caso o número já exista lá dentro, ele não será adicionado.
4° No final, serão exibidos todos os valores únicos digitados, em ordem crescente.'''

valoresnum = []

while True:
    valoresnum.append(int(input('Digite um valor: ')))

    for i,v in enumerate(valoresnum):
        contagem = valoresnum.count(v)
        if contagem >= 2:
            print('\033[33mVALOR DUPLICADO!!\033[m\n\033[33;40m-> Não vou adicionar.\033[m')
            valoresnum.remove(v)

    continuar = str(input('Deseja continuar? [S/N]')).upper().strip()
    if continuar == 'N':
        break
valoresnum.sort()
print('='*30)
print('Você digitou esses números:',end='')
print(valoresnum)
