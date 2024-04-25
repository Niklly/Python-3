print('\033[1;34m{:-^26}\033[m'.format('AVALIANDO PESOS'))
maior = 0
menor = 0
for pess in range(1,6):
    peso = float(input('P{}: Digite o seu peso (kg): '.format(pess)))
    if pess == 1:    #aqui eu to analisando como se existisse só a primeiro peso, logo ele vai ser tanto maior e menor
        menor = peso   #ele é maior pois ainda não li outros pesos
        maior = peso
    else:
        if peso > maior:  #agora, se eu li um peso maior do que o primeiro, ele vai se tornar o maior. Assim, sucessivamente
            maior = peso
        if peso < menor:
            menor = peso
print('O menor peso foi {}kg'.format(menor))
print('O maior peso foi {}kg'.format(maior))



