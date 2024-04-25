from datetime import date

ano = int(input('Digite o ano de seu nascimento: '))
data = date.today().year
idade = data - ano

print('Quem nasceu em {} tem {} anos em {}.'.format(ano, idade, data))

if idade == 18:
    print('\033[31mATENÇÃO!!\033[m Você terá que se alistar esse ano ao serviço militar..')

elif idade < 18:
    tempo = 18 - idade
    print('Ainda falta(m) \033[34m{} ano(s)\033[m para você se alistar ao exército.'.format(tempo))

else:
    tempo = idade - 18
    print('Já se passaram \033[34m{} ano(s)\033[m que você teve que se alistar.'.format(tempo))




