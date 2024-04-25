peso = float(input('Qual o seu peso \033[35m(kg): \033[m'))
altura = float(input('Qual a sua altura \033[35m(m): \033[m'))

imc = peso / (altura*altura)

if imc < 18.5:
    print('Você está: \033[34mABAIXO DO PESO.\033[m')
elif 18.5 <= imc < 25:
    print('Você está: \033[32mPESO IDEAL.\033[m')
elif 25 <= imc < 30:
    print('Você está: \033[33mSOBREPESO.\033[m')
elif 30 <= imc < 40:
    print('Você está: \033[35mACIMA DO PESO.\033[m')
elif imc >= 40:
    print('Você está: \033[36mOBESIDADE MÓRBIDA.\033[m')



