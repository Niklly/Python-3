from datetime import date

ano = int(input('Digite o ano de seu nascimento: '))
data = date.today().year
idade = data - ano

print('O atleta possui {} anos.'.format(idade))
if idade <= 9:
    print('Você se encontra na categoria:\033[31mMIRIM\033[m')
elif idade <= 14:
    print('Você se encontra na categoria:\033[32mINFANTIL\033[m')
elif idade <= 19:
    print('Você se encontra na categoria:\033[33mJUNIOR\033[m')
elif idade <= 25:
    print('Você se encontra na categoria:\033[34mSÊNIOR\033[m')
else:
    print('Você se encontra na categoria:\033[35mMASTER\033[m')



