import random

n1 = input('Digite o nome do primeiro aluno: ')
n2 = input('Digite o nome do segundo aluno: ')
n3 = input('Digite o nome do terceiro aluno: ')
n4 = input('Digite o nome do quarto aluno: ')

lista = [n1, n2, n3, n4]
ordem = random.sample(lista,4)
print('A ordem de apresentação dos alunos será: {}'.format(ordem))


# ou posso fazer o seguinte: lista = [n1,n2,n3,n4]
# embaixo eu uso o random.shuffle(lista) e pedir um print da lista(irá embaralhar)