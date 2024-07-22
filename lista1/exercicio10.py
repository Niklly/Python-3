nota1 = float(input("Digite a nota da prova 1: "))
nota2 = float(input("Digite a nota da prova 2: "))
nota3 = float(input("Digite a nota da prova 3: "))

media = (nota1 + nota2 + nota3) / 3

if media >= 7.0:
    print("O aluno foi aprovado.")

elif media < 7.0:
    mediaFinal = float(input("Digite a nota da prova final:"))
    if mediaFinal >= 5.0:
        print("O aluno foi aprovado.")
    else:
        print("Reprovou.")
