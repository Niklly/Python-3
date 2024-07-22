lados = int(input(f"Digite o número de lados de um polígono regular:"))
valor = int(input(f"Digite a medida do lado: "))

if lados == 3:
    perimetro = valor * 3
    print("Triangulo, o valor do perimetro é", perimetro)

elif lados == 4:
    area = valor * valor
    print("Quadrado, o valor da area é", area)

elif lados == 5:
    print("Pentagono")

else:
    print("Poligono nao identificado")