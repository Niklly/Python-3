######################################################
# Programação Funcional / Programção I (2022/2)
# EP2 - Jogo da Velha
# Nome: Nikelly Silva de Jesus 
# Matrícula:2021202011
######################################################

import random
from os import system, name 

def getMatricula():
    """
    Retorna a matricula do aluno como string
    """
    return "2021202011" 

def getNome():
    """
    Retorna o nome completo do aluno
    """
    return "Nikelly Silva de Jesus" 

def limpaTela(): 
	if name == 'nt': 
		system('cls') 
	else: 
		system('clear') 

def imprimetabuleiro(tab):

    print(" "+tab[7]+" | "+tab[8]+" | "+tab[9])
    print("---+---+---")
    print(" "+tab[4]+" | "+tab[5]+" | "+tab[6])
    print("---+---+---")
    print(" "+tab[1]+" | "+tab[2]+" | "+tab[3])

def entrada():
    
    simbolo_j = input(f"Você quer ser X ou O?")
    
    if simbolo_j == "X" or simbolo_j == "x":    
        simbolo_j = "X"
        simbolo_pc = "O"
        return simbolo_j, simbolo_pc

    elif simbolo_j == "O" or simbolo_j == "o":
        simbolo_j = "O"
        simbolo_pc = "X"
        return simbolo_j, simbolo_pc

    else:
        print("Digite um caractere valido..")
        return entrada() 
    

def Verifica_quem_ganhou(tab,simbolo_j,simbolo_pc):


    #possibilidades do jogador ganhar.

    #linha
    if  tab[1]== simbolo_j and tab[2]==simbolo_j and tab[3]== simbolo_j:
        return 1
    elif tab[4] == simbolo_j and tab[5]==simbolo_j and tab[6]==simbolo_j:
        return 1
    elif tab[7] == simbolo_j and tab[8]==simbolo_j and tab[9]==simbolo_j:
        return 1
    
    #coluna
    elif tab[1] == simbolo_j and tab[4]==simbolo_j and tab[7]==simbolo_j:
        return 1
    elif tab[2] == simbolo_j and tab[5]==simbolo_j and tab[8]==simbolo_j:
        return  1
    elif tab[3] == simbolo_j and tab[6]==simbolo_j and tab[9]==simbolo_j:
        return 1

    #diagonal
    elif tab[1] == simbolo_j and tab[5]==simbolo_j and tab[9]==simbolo_j:
        return 1
    elif tab[3] == simbolo_j and tab[5]==simbolo_j and tab[7]==simbolo_j:
        return 1

#possibilidades do computador ganhar

    #linha
    elif tab[1] == simbolo_pc and tab[2]==simbolo_pc and tab[3]==simbolo_pc:
        return 0
    elif tab[4] == simbolo_pc and tab[5]==simbolo_pc and tab[6]==simbolo_pc:
        return 0
    elif tab[7] == simbolo_pc and tab[8]==simbolo_pc and tab[9]==simbolo_pc:
        return 0

    #coluna
    elif tab[1] == simbolo_pc and tab[4]==simbolo_pc and tab[7]==simbolo_pc:
        return 0
    elif tab[2] == simbolo_pc and tab[5]==simbolo_pc and tab[8]==simbolo_pc:
        return  0
    elif tab[3] == simbolo_pc and tab[6]==simbolo_pc and tab[9]==simbolo_pc:
        return 0

    #diagonal

    elif tab[1] == simbolo_pc and tab[5]==simbolo_pc and tab[9]==simbolo_pc:
        return 0
    elif tab[3] == simbolo_pc and tab[5]==simbolo_pc and tab[7]==simbolo_pc:
        return 0
    else:
        return

def jogadasjogador(tab,simbolo_j):

    posicao = int(input("Digite uma posição (1-9):"))

    if tab[posicao] == ' ':
        tab[posicao] = simbolo_j
    elif   posicao > 9:
        print("Digite uma posição livre.")
        jogadasjogador(tab,simbolo_j)
    
    else:
        print("Digite uma posição válida.")
        jogadasjogador(tab,simbolo_j)

def jogo(tab,simbolo_pc,simbolo_j,jogadas_jogador,i):
    
    if i in jogadas_jogador:
        jogadasjogador(tab,simbolo_j)
        imprimetabuleiro(tab)
        if (Verifica_quem_ganhou(tab,simbolo_j,simbolo_pc)== 1):
            print("Parabéns você ganhou!!!")
            return
        else:
            jogo(tab,simbolo_pc,simbolo_j,jogadas_jogador,i=i+1)

    elif (i==9):
        print("EMPATE")
        return
    
    else:
        jogadacomputador(tab,simbolo_pc)
        imprimetabuleiro(tab)  
        if (Verifica_quem_ganhou(tab,simbolo_j,simbolo_pc) == 0):
            print("O pc ganhou.")
            return
        else:
            jogo(tab,simbolo_pc,simbolo_j,jogadas_jogador,i=i+1)

def jogadacomputador(tab,simbolo_pc):    
    
    #coluna 1
    if (tab[1]==tab[4] and tab[7]==" "):
        tab[7] = simbolo_pc
    elif (tab[1]==tab[7] and tab[4]==" "):
        tab[4] = simbolo_pc
    
    elif (tab[1]==tab[7] and tab[4]==" "):
        tab[4] = simbolo_pc
    
    #coluna 2
    elif (tab[2]==tab[5] and tab[8]==" "):
        tab[8] = simbolo_pc
    
    elif (tab[5]==tab[8] and tab[2]==" "):
        tab[2]=simbolo_pc

    elif (tab[2]==tab[8] and tab[5]==" "):
        tab[5]=simbolo_pc
    
    #coluna 3

    elif (tab[3]==tab[6] and tab[9]==" "):
        tab[9]=simbolo_pc

    elif (tab[9]==tab[6] and tab[3]==" "):
        tab[3]=simbolo_pc
    
    elif (tab[3]==tab[9] and tab[6]==" "):
        tab[6]=simbolo_pc

    #linha 1
    elif (tab[1]==tab[2] and tab[3]==" "):
        tab[3]=simbolo_pc

    elif (tab[2]==tab[3] and tab[1]==" "):
        tab[1]=simbolo_pc

    elif (tab[1]==tab[3] and tab[2]==" "):
        tab[2]=simbolo_pc
    
    #linha2

    elif (tab[4]==tab[5] and tab[6]==" "):
        tab[6]=simbolo_pc
    
    elif (tab[5]==tab[6] and tab[4]==" "):
        tab[4]=simbolo_pc
    
    elif (tab[4]==tab[6] and tab[5]==" "):
        tab[5]=simbolo_pc
    
    #linha3

    elif (tab[7]==tab[8] and tab[9]==" "):
        tab[9]=simbolo_pc

    elif (tab[8]==tab[9] and tab[7]==" "):
        tab[7]=simbolo_pc

    elif (tab[7]==tab[9] and tab[8]==" "):
        tab[8]=simbolo_pc
    
    #diagonal1
    elif (tab[1]==tab[5] and tab[9]==" "):
        tab[9]=simbolo_pc
    elif (tab[5]==tab[9] and tab[1]==" "):
        tab[1]=simbolo_pc
    elif (tab[1]==tab[9] and tab[5]==" "):
        tab[5]=simbolo_pc
    
    #diagonal2
    elif (tab[7]==tab[5] and tab[3]==" "):
        tab[3]=simbolo_pc

    elif (tab[5]==tab[3] and tab[7]==" "):
        tab[7]=simbolo_pc

    elif (tab[7]==tab[3] and tab[5]==" "):
        tab[5]=simbolo_pc
    
    else:
       aleatoriamente(tab,simbolo_pc)

def aleatoriamente(tab,simbolo_pc):

    aleatorio = random.choice(range(1,10))
    if tab[aleatorio] == " ":
        tab[aleatorio] = simbolo_pc
    else:
        return aleatoriamente(tab,simbolo_pc)
    
def main():
    limpaTela()

    tab = [' ']*10
    tab[0] = "invalido"
    simbolo_j,simbolo_pc = entrada()
    Numeros = [0,1] #será sorteado que será 1 ou 0. Logo se X == 1, ele começa.
    quem_começa = random.choice(Numeros)
    jogadas_jogador = list(range(quem_começa,9,2))
    jogo(tab[:],simbolo_j,simbolo_pc,jogadas_jogador,0)

################################
## NÃO ALTERE O CÓDIGO ABAIXO ##
################################
if __name__ == "__main__":


    main()


    

















