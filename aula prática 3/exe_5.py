contaPar = 0
contaImpar = 0

x = int(input("Digite um número: "))
if x%2 == 0:
    contaPar += 1 # contaPar = contaPar +1
else:
    contaImpar +=1

x = int(input("Digite um numero: "))
if x%2 == 0:
    contaPar += 1 
else:
    contaImpar +=1

x = int(input("Digite um numero: "))
if x%2 == 0:
    contaPar += 1
else:
    contaImpar +=1

x = int(input("Digite um numero: "))
if x%2 == 0:
    contaPar += 1
else:
    contaImpar +=1

conta = contaImpar * contaPar
print(f"Foram digitados {contaPar} números pares, e {contaImpar} números impares.")
print(f" A mutiplicação entre os números pares e ímpares é {conta}")