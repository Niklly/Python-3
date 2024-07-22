def calcular(n,p):

    import math
    s = (n - p)

    n1 = math.factorial(n)
    p1 = math.factorial(p)
    s1 = math.factorial(s)

    c = n1 / (s1 * p1)

    if p <= n:
        print("O numero de combinações possíveis :", c)
    
    else:
        print("ERRO.")

def main():

    n = int(input("Digite um numero qualquer para n: "))
    p = int(input("Digite um valor para p: "))
    calcular(n,p)

main()

