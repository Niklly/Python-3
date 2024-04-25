print('\033[37;35;40m{:-^30}\033[m'.format('TABUADA DO PYTHON'))
n = int(input('Tabuada do número: '))

for c in range(1,11):
    t = c * n
    print('{} X {} = {}'.format(n,c,t))



