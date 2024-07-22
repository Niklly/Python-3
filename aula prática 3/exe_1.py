media = float(input("Digite a media do aluno:"))

if media < 0 or media > 10.0:
    print("ERRO")

elif media >= 9.0:
    print("A")

elif media >= 8.0 and media < 9.0:
    print("B")

else :
    if media >= 7.0 and media < 8.0:
        print("C")

    elif media >= 6.0 and media < 7.0:
        print("D")
        
    else :
        print("R")

