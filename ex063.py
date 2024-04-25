termos = int(input('Digite a quantidade de termos que quer: '))

t1 = 0
t2 = 1
contador = 3
print(f'{t1} -> {t2} ->', end='')
while contador <= termos:
    t3 = t1 + t2
    contador += 1
    t1 = t2
    t2 = t3
    print(' {} ->'.format(t3), end='')

print(' FIM')
