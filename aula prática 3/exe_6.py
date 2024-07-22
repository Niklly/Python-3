semErro = True

x = int(input("Digite um numero qualquer:"))

if x >= 0 and x <= 5:
    print("Falha do tipo 1")
    semErro = False

if x < 0:
    print("Falha do tipo 2")
    semErro = False

if x // 3 and x % 6 == 0:
    print("Falha do tipo 3")
    semErro = False

if  x ==  7 :
    print("Falha do tipo 100")
    semErro = False

if semErro:
    print("Sistema funcionando normalmente")
    
