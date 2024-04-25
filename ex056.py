soma = 0
menina = 0
maioridadehomem = 0
nomevelho = ''

for pess in range(1,5):
    print('-'*5, '{}° PESSOA'.format(pess), 5*'-')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [F/M]: ')).strip().lower()
    soma += idade

    if sexo == 'f' and idade < 20:
        menina += 1

    if sexo == 'm' and pess == 1:
        idade = maioridadehomem
        nomevelho = nome

    if sexo == 'm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome

media = soma/4
print('A média de idade do grupo é de {} anos '.format(media))
print('Existe(m) {} mulher(es) com menos de 20 anos.'.format(menina))
print('O homem mais velho possui {} anos. E se chama {}.'.format(maioridadehomem, nomevelho))





