n = float(input('Escreva um valor em metros: '))
#   km hm dam m dm cm mm
dm = n*10
cm = n*100
mm = n*1000
dam = n/10
hm = n/100
km = n/1000




print('O valor de {}m equivale a: \n{:.1f} milimetros \n{:.1f} centimetros \n{:.1f} decimetros \n {:.1f} decametros \n {:.2f} hectometros \n {:.3f} kilometros'.format(n,mm,cm,dm,dam,hm,km))