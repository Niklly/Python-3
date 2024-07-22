def imprime(L=[], i=0, soma = 0):
    if i < len(L):
        print(L[i])
        imprime( i+1, soma + L)
    else:
        return soma, soma/len(L)
     
        
def main():
    lista = [1,2,3,4]
    imprime(lista)

main()