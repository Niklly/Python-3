print('-' * 30)
print('{:^30}'.format('CADASTRE UMA PESSOA'))
print('-' * 30)
adulto = homem = mulher = 0
while True:
    sexo = ' '
    continuar = ' '
    idade = int(input('Idade: '))
    if idade > 18:
        adulto += 1
    while sexo not in 'MFmf':
        sexo = str(input('Sexo [F/M]: ')).strip().upper()
        if sexo == 'M':
            homem += 1
        if sexo == 'F':
            if idade < 20:
                mulher += 1
    while continuar not in 'SNsn':
        continuar = str(input('\033[7;38;40mVocê quer continuar [S/N]:\033[m')).strip().upper()
        print('-' * 25)
    if continuar == 'N':
        break

print('{:-^15}'.format('FIM DO PROGRAMA'))
print(f'Total de pessoas com maiores de 18 anos: \033[33m{adulto}\033[m')
print(f'Total de homens cadastrados: \033[33m{homem}\033[m')
print(f'Total de mulheres com menos de 20 anos: \033[33m{mulher}\033[m')












