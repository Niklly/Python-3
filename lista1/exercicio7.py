n =  int(input("Digite um valor entre 100 e 999."))

n1 = n // 100
print("centena", n1)

n2 = (n % 100) // 10
print("dezena", n2)

n3 = n % 10
print("unidade", n3)

if n >= 100 and n <= 999:
    if n1<n2<n3:
        print("Esse numero e ascendente.")

    else:
        print("Erro.")