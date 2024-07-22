n = int(input("Digite um número: "))
n1 = n //100
print("centena: ", n1)
n2 = (n % 100) // 10
print("Dezena: ", n2)
n3 = n % 10 
print("Unidade: ", n3)


if (n >= 100) and (n <= 999):
    if n1<n2<n3:
        print("Esse número é ascendente.")
    else:
        print("Não é ascendente")
        
