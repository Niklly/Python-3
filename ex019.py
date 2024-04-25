import random

aluno_a = input('Qual o nome do primeiro aluno? ')
aluno_b = input('Qual o nome do segundo aluno? ')
aluno_c = input('Qual o nome do terceiro aluno? ')
aluno_d = input('Qual o nome do quarto aluno? ')

escolha = [aluno_a, aluno_b, aluno_c, aluno_d]
escolhido = random.choice(escolha)
print('O aluno escolhido para limpar o quadro é {}'. format(escolhido))

