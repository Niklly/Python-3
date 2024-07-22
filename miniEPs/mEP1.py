A = int(input())
B = int(input())
C = int(input())

# Identificação do maior lado
if A >= B and A >= C:
    maior = A
    outro_1 = B
    outro_2 = C
elif B >= A and B >= C:
    maior = B
    outro_1 = A
    outro_2 = C
else:
    maior = C
    outro_1 = A
    outro_2 = B

# Definindo o triângulo
if maior <= 0 or outro_1 <= 0 or outro_2 <= 0:
    print("Valores invalidos.")
elif maior >= outro_1 + outro_2:
    print("Valores nao podem formar um triangulo.")
else:
    # Classificação quanto aos lados
    if maior == outro_1 and maior == outro_2:
        print("Triangulo equilatero.")
    elif maior == outro_1 or maior == outro_2 or outro_1 == outro_2:
        print("Triangulo isosceles.")

    else:
        print("Triangulo escaleno.")
    
# Classificação quanto ao ângulo
    if maior**2 == outro_1**2 + outro_2**2:
        print("Triangulo retangulo.")
    elif maior**2 > outro_1**2 + outro_2**2:
        print("Triangulo obtusangulo.")
    else:
        print("Triangulo acutangulo.")