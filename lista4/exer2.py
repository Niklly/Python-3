def leitura(L, i=0, cont =0):   
    if i < len(L):
        cont += L[i]
        return leitura(L, i+1, cont)
    else:
        media = len(L)
        return cont/media

def main():
    L=[1,-2,3,4]
    print(leitura(L))

main()



