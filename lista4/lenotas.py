def lenotas(n, notas =[]):
    x = float(input("Nota:"))
    if len(notas) == n:
        return notas
    else:
        if x >= 0:
            return lenotas(n, notas+[x])
        else:
            return n,notas+[x]

def main():

    print(lenotas())

main()