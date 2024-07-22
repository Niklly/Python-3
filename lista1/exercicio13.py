a = int(input(f"Digite um valor para a :"))
b = int(input(f"Digite um valor para b : "))
c = int(input(f"Digite um valor para c : "))

if (b - c) < a < (b + c) or (a - c) < b < (a + c) or (a - b) < c < (a + b):
    print("Pode se formar um triangulo. ")
    if a == b == c:
        print("Triangulo equilatero.")

    elif a == b or b == c or a == c:
                print("Triangulo isósceles.")

    elif a != b and b != c and a != c:
                print("Triangulo escaleno.")

else:
    print("Não podemos formar um triangulo.")
