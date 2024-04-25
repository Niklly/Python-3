from time import sleep

print('=-' * 20)
print('{:^40}'.format('CONTAGEM REGRESSIVA PARA OS FOGOS'))
print('=-' * 20)

for c in range(10,-1,-1):
    print(c)
    sleep(1)
print('\033[35mFELIZ ANO NOVO!!!\033[m')
