casa = float(input("Digite o valor inteiro da casa que quer comprar:"))
salario = float(input("Digite seu salário mensal:"))
tempo = float(input("Digite em quanto anos quer pagar a casa:"))

# 1 ano = 12  meses
# 2 anos =  24 meses
# 3 anos = 36 meses

meses = (tempo * 12)
parcela = (casa / meses)

salario30 = (salario * (3/10))

if parcela > salario30:
    print("O empréstimo não foi aprovado.")

else:
    print("PARABÉNS.")