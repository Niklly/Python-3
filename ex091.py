from random import randint
from time import sleep
from operator import itemgetter

jogadores = dict()
resultado = list()

jogadores['jogador 1'] = randint(1,6)
jogadores['jogador 2'] = randint(1,6)
jogadores['jogador 3'] = randint(1,6)
jogadores['jogador 4'] = randint(1,6)

print("=*" * 25)
print("Valores sorteados: ")
for k, v in jogadores.items():
    print(f"O {k} tirou {v} no dado.")
    sleep(1)


resultado = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
print("=== Ranking dos jogadores ===")

for i, v in enumerate(resultado):
    print(f"{i+1}° lugar: {v[0]} com {v[1]}")
    sleep(1)