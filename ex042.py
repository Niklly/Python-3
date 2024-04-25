print('\033[7;38m*\033[m'*36)
print('\033[7;38;40m '*4, 'CLASSIFICADOR DE TRIÂNGULO', ' '*3,'\033[m')
print('\033[7;38m*\033[m'*36)

a = float(input('Primeiro lado: '))
b = float(input('Segundo lado: '))
c = float(input('Terceiro lado: '))

if a < b + c and b < a + c and c < a + b:
    if a == b == c:
        print('Esse triangulo é:\033[34mEQUILATERO\033[m')
    elif a != b != c != a:
        print('Esse triangulo é:\033[35mESCALENO\033[m')
    else:
        print('Esse triangulo é:\033[36mISÓSCELES\033[m')

else:
    print('Os lados \033[31mNÃO\033[m podem formar um triangulo.')

