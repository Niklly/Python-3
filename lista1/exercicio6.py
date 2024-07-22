n = int(input("Digite um numero entre 1000 a 9999:"))

n1 = n // 1000
print("Milhar:", {n1})
n2 = (n % 1000) // 100
print("Centena:", {n2})
n3 = (n % 100) // 10
print("Dezena:", {n3})
n4 = n % 10
print("Unidade:", {n4})

if  n >= 1000 and n <= 9999:
    if (n1 == n2 == n3 == n4) or (n1 == n4 and n2 == n3):
        print("Esse numero é polidromo.")

    else:
        print("ERRO")