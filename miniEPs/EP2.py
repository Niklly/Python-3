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

def entrada2():
    
    simbolo_j = input(f"Você quer ser X ou O?")

    ##Este "if" SEMPRE vai retornar simbolo_j="X" e simbolo_pc="0"
    
    if simbolo_j == "X" or "x":    
        simbolo_j = "X"
        simbolo_pc = "O"
        return simbolo_j, simbolo_pc

    elif simbolo_j == "O" or "o":
        simbolo_pc = "X"
        simbolo_j = "O"
        return simbolo_j, simbolo_pc

    else:
        print("Digite um caractere valido..")
        return entrada() 

def entrada():
    
    simbolo_j = input(f"Você quer ser X ou O?")
    
    if simbolo_j in ["X", "x"]:
        simbolo_j = "X"
        simbolo_pc = "O"
        return simbolo_j, simbolo_pc

    elif simbolo_j in ["O", "o", "0"]:
        simbolo_pc = "X"
        simbolo_j = "O"
        return simbolo_j, simbolo_pc

    else:
        print("Digite um caractere valido..")
        return entrada()

"""
def entrada():
    
    simbolo_j = input(f"Você quer ser X ou O?")
    
    if simbolo_j=="X" or simbolo_j=="x":
        simbolo_j = "X"
        simbolo_pc = "O"
        return simbolo_j, simbolo_pc

    elif simbolo_j=="O", or simbolo_j=="o":
        simbolo_pc = "X"
        simbolo_j = "O"
        return simbolo_j, simbolo_pc

    else:
        print("Digite um caractere valido..")
        return entrada() 

"""

def joga_primeiro():
#Esta funcao nao tem utilidade, basta com as dois primeiras linhas o "if" é redundante.
    Nuemros = [0,1] # 0 = bot  1 = player
    Quem_Joga = random.choice(Nuemros)
    if Quem_Joga == 1:
        return 1
    else:
        return 0

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
    elif  1 < posicao > 9:
        print("Digite uma posição livre.")
        jogadasjogador(tab,simbolo_j)
    """
    O que acontece se o jogador nao ingresa um número?
    Se o jogador ingresa uma "k" este "if-else" gerara erro.
    """ 
    
    """
    Esta linha diz: se a posicao > 9 imprima "Digite uma posicao livre".
    Nao esta mal, porque se esse número é maior que 9 nao tem onde colocar"
    """  

def jogo(tab,simbolo_pc,simbolo_j,quemjoga,i):
    """
    Esta funcao nao tem alternar o jogo. quem joga aqui é um número fixo. 
    """
    if quemjoga == 1:
        jogadasjogador(tab,simbolo_j)
        imprimetabuleiro(tab)
        if (Verifica_quem_ganhou(tab,simbolo_j,simbolo_pc)== 1):
            print("Parabéns você ganhou!!!")
            return
        else:
            jogo(tab,simbolo_pc,simbolo_j,0,i=i+1)
    elif quemjoga == 0:
        jogadacomputador(tab,simbolo_pc)
        imprimetabuleiro(tab)  ##Agregada
        if (Verifica_quem_ganhou(tab,simbolo_j,simbolo_pc) == 0):
            print("O pc ganhou.")
            return
        else:
            jogo(tab,simbolo_pc,simbolo_j,1,i=i+1)
    elif (i>=9):
        print("EMPATE")
        return

def jogadacomputador(tab,simbolo_pc):    
    """
    if (tab[1]==tab[4] ) :
        if tab[7]==" ":
            return simbolo_pc == tab[1] ##Isto é um "bool"
            aqui gera um erro em caso que nao esté vazio
    """
    #####Recomendo este:
    if (tab[1]==tab[4] and tab[7]==" "):
        tab[7] = simbolo_pc
    elif (tab[1]==tab[7] and tab[4]==" "):
        tab[4] = simbolo_pc
    #elif
        #....
    #else:
        ###UMA FUNCAO PARECIDA A ALEATORIO
        

    

def main():
    limpaTela()
    tab = [' ']*10
    tab[0] = "invalido"
    simbolo_j,simbolo_pc = entrada()
    quemjoga = joga_primeiro()
    jogo(tab[:],jogadasjogador,simbolo_j,quemjoga)

################################
## NÃO ALTERE O CÓDIGO ABAIXO ##
################################
if __name__ == "__main__":
    #main()


#""""PRUEBA
    simbolo_j,simbolo_pc = entrada()
    Nuemros = [0,1] # 0 = bot  1 = player
    quemjoga = random.choice(Nuemros)
    tab = [' ']*10
    tab[0] = "invalido"
    jogo(tab,simbolo_pc,simbolo_j,quemjoga,0)
#""""
    

















