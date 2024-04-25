from datetime import date
data = date.today().year
a = 0
j = 0
print('\033[36m{:-^25}\033[m'.format('MAIORIDADE BRASIL'))
for c in range(1,8):
    ano = int(input('P{}: Qual o seu ano de nascimento: '.format(c)))
    if data - ano >= 21:
        a += 1
    else:
        j += 1
print('O total de \033[34mpessoas maiores\033[m de 18 anos: {}'.format(a))
print('O total de \033[33mpessoas menores\033[m de 18 anos: {}'.format(j))



