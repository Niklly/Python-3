a = float(input('Primeiro segmento: '))
b = float(input('Segundo segmento: '))
c = float(input('Terceiro segmento: '))

if b < a + c and a < b + c and c < a + b:
    print('Os segmentos PODEM formar um triangulo')
else:
    print('Os segmentos NÃO PODEM formar um triangulo.')

