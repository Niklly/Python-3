import math

angulo = float(input('Digite um ângulo qualquer: '))

seno = math.sin(math.radians(angulo))
cos = math.acos(math.radians(angulo))
tan = math.tan(math.radians(angulo))

print('O angulo de {} possui o valor de\nSENO: {:.2f}\nCOSSENO: {:.2f}\nTANGENTE: {:.2f}'.format(angulo, seno, cos, tan))


