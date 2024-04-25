nome = str(input('Qual é seu nome completo?')).strip()
corrigido = nome.title()
print('Seu nome tem Silva? {}'.format('Silva' in corrigido))
