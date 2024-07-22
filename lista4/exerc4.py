def leitura(soma = 0, qt =0):
    n =float(input("Digite uma nota: :"))
    if n < 0 or n > 10:
        return soma + n, qt + 1
    else:
        return leitura(soma + n, qt + 1)

def main():
    soma,qt = leitura()
    print("Quantidade de notas lidas:",qt)
    print("Soma de todas as notas: ", soma)
    if qt > 0:
        print("media das notas: ", soma/qt)
    
main()