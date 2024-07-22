

def imprime(L, i=0):
    if i < len(L):
        print(L[i])
        imprime(L, i+1)

def main():
    lista = [1,2,3,4]
    lista.reverse()
    print(imprime(lista))
    

main()