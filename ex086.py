matriz = [[0,0,0], [0,0,0], [0,0,0]]

# essa matriz é para receber os valores que estou digitando
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f'Digite um valor em [{l}, {c}]: '))

print("=-"*25)
# essa matriz é para mostrar os valores que eu estou substituindo por zero
for l in range(0,3): #para cada linha
    for c in range(0,3): #para cada coluna
        print(f'[{matriz[l][c]:^5}]',end='')
    print() #aqui eu vou pular uma linha quando finalizar a coluna



