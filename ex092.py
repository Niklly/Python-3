from datetime import date

trabalhador = dict()

trabalhador["nome"] = str(input("Nome: "))
nascimento = int(input("Ano de nascimento: "))
trabalhador["ctps"] = int(input("Carteira de trabalho (0 não tem): "))
trabalhador["idade"] = date.today().year - nascimento

if trabalhador["ctps"] != 0:
    trabalhador["contratação"] = int(input("Ano de contratação: "))
    trabalhador["salario"] = int(input("Salário: R$"))
    trabalhador["aposentadoria"] = (trabalhador["contratação"] + 35) - nascimento

print("*="*25)
for k,v in trabalhador.items():
    print(f"-{k} tem o valor {v}.")

