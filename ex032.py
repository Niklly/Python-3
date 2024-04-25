from datetime import date

ano = int(input('Qual ano quer analisar? Digite 0 para analisar o ano atual: '))

if ano == 0:
    ano = date.today().year #vou analisar o ano atual através de uma importação da função

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO!'.format(ano))

else:
    print('O ano {} NÃO É BISSEXTO!'.format(ano))

