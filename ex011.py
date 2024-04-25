l = float(input('Digite a largura da parede (em metros): '))
a = float(input('Digite o altura da parede (em metros): '))

area = l * a
tinta = area/2

print('A quantidade necessária de tinta será {:.2f} litros para pintar a parede de {:.2f}m².'.format(tinta,area))