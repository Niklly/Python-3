'''import math
from math import sqrt, pow
o = float(input('Digite o valor do cateto oposto: '))
a = float(input('Digite o valor do cateto adjacente: '))
oposto = pow(o,2)
adjacente = pow(a,2)

h = (oposto + adjacente)
print('O valor da hipotenusa é {:.2f}'.format(sqrt(h)))'''



# jeito feito sem importação math
co = float(input('Digite o valor do cateto oposto: '))
ca = float(input('Digite o valor do cateto adjacente: '))

hipo = ((co ** 2) + (ca ** 2)) ** (1/2)
print('O valor da hipotenusa é {:.2f}'.format(hipo))