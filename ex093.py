jogador = dict()

k = 0

jogador["nome"] = str(input("Nome do jogador: "))
partidas = int(input(f"Quantas partidas {jogador['nome']} jogou? "))

if partidas != 0:
    while partidas > k:
        k += 1
        gol = int(input(f"Quantos gols na partida {k}? "))
        gols.append(gol)

print(jogador,gols)