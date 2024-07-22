print(" Digite a data de nascimento:")
diaN = int(input(f"-> Dia? "))
mesN = int(input(f"-> Mês? "))
anoN = int(input(f"-> Ano? "))

print("Digite a data atual:")
dia = int(input(f"-> Dia? "))
mes = int(input(f"-> Mês? "))
ano = int(input(f"-> Ano? "))

Idade = ano - anoN

if mes < mesN:
    idade = (ano - anoN) - 1
    print("Idade:", idade, "anos")

elif mes == mesN and dia < diaN:
    idade = (ano - anoN) - 1
    print("Idade:", idade, "anos")

else:
    print("Idade:", Idade, "anos")
