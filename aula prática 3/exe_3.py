from re import X
import string


Jogador1 = input(f"Quem você quer ser X ou O:")

if Jogador1 == "X" :
    print("Jogador2 será O.")

if Jogador1 == "O":
    print("Jogador2 será X.")


# O jogo real não precisa ser apenas X ou O. Os jogadores podem usar simbolos e outras letras.