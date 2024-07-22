def leitura(soma=0):
    
    n = float(input("Digite valores: "))
        
    if n < 0:
        return soma
    else:
        return leitura(soma+n)
    
def main():
    soma = leitura()
    print("A soma dos numeros lidos: ",soma)

main()

