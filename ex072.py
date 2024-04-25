extenso = 'zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quartoze','quinze','dezesseis','dezessete','dezeoito','dezenove','vinte'

num = int(input('Digite o número: '))
while True:
    if 0 <= num <= 20:
        print(extenso[num])
        break

    else:
        tentativa = int(input('Tente novamente: '))
        if 0 <= tentativa <= 20:
            print(extenso[tentativa])
            break

print('fim do programa.')






