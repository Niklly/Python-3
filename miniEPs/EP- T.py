import random
from os import system, name 

def getMatricula():
    """
    Retorna a matricula do aluno como string
    """
    return "2020102526" 

def getNome():
    """
    Retorna o nome completo do aluno
    """
    return "THARCISIO DA COSTA ASSIS" 

def limpaTela(): 
	if name == 'nt': 
		system('cls') 
	else: 
		system('clear') 

def defSimbulo( ):
    """
    Solicita ao usuário(jogador) a escolha de uma letra (X ou O) para representá-lo no tabuleiro:
        1) Se escolhido o X, é atribuído o O ao oponente
        2) Se escolhido o O, é atribuído o X ao oponente
        3) Se recebida uma letra ou simbolo inválido a função chama a si mesma recursivamente
            até que receba uma letra válida
    Retorno:
    jogador1: letra que representa o primeiro jogador
    jogador2: letra que representa o segundo jogador

    """
    s = input("Informe com qual letra (X ou O) deseja jogar: ")
    if s == "X" or s =="x":
        jogador1 = "X"
        jogador2 = "O"
        return jogador1, jogador2
    elif s == "O" or s =="o":
        jogador1 = "O"
        jogador2 = "X"
        return jogador1, jogador2
    else:
        print("símbolo inválido")
        return defSimbulo( )

def sorteio():
    """
    Sorteia a ordem em que jogarão os jogadores (no caso, usuário(Jogador) e Computador)

    Retorno:
    jogador1: primeiro a jogar
    jogador2: segundo a jogar
    """
    from random import randint
    if randint(1,2) == 1:
        jogador1 = "Jogador"
        jogador2 = "Computador"
    else: 
        jogador1 = "Computador"
        jogador2 = "Jogador"
    return jogador1, jogador2

def tabuleiroImpressao(tabuleiro):
    """
    Imprime o desenho do tabuleiro posicionando os índices da lista nas seus respectivos lugares.

    Parâmetro:
    tabuleiro: lista de tamanho 10 representando o tabuleiro
    """
    print (f" {tabuleiro[7]} | {tabuleiro[8]} | {tabuleiro[9]} ")
    print("-----------")
    print (f" {tabuleiro[4]} | {tabuleiro[5]} | {tabuleiro[6]} ")
    print("-----------")
    print (f" {tabuleiro[1]} | {tabuleiro[2]} | {tabuleiro[3]} ")

def posicao_escolhidaJ():
    """
    Solicita a escolha de uma posição(índice) a ser marcada/ocupada e verifica de é válida(entre 1 e 9):
        1) Se sim, retorna a posição
        2) Se não, chama recursivamente a si mesme até que seja dada entrada de uma posição válida
    """

    posicao =  int(input("Informe onde deseja jogar: "))
    if 1<=posicao<=9:
        return posicao
    else:
        print("Posicao invalida")
        return posicao_escolhidaJ()

def jogadaComputador(tabuleiro, simboloComputador):
    """
    Recebe o tabuleiro e o simbolo (X ou O) do computador e determina onde o computador deve jogar
    O tabuleiro pode estar vazio (caso o computador seja o primeiro a jogar) ou com algumas posições preenchidas, 
    sendo a posição 0 do tabuleiro descartada.

    Parâmetros:
    tabuleiro: lista de tamanho 10 representando o tabuleiro
    simboloComputador: letra do computador

    Retorno:
    Posição (entre 1 e 9) da jogada do computador

    Estratégia:
    Antes de marcar um local(índice) qualquer livre (na sequência que estabeleci de acordo com o meu modo de jogar 
    e informações obtidas nos testes de execução), o código verifica se o oponente está próximo de vencer (com uma
    sequência de duas letras consecutivas (XX ou OO, de acordo com a letra que o representa) ou sequência de duas 
    letras alternadas (X, ,X ou O, ,O)),  se estiver: marca/ocupa o índice necessário para o oponente vencer, assim
    o impedindo.
    """
#________________________________________________________________________________________________________________________
    if (tabuleiro[1] == simboloComputador and tabuleiro[2] == simboloComputador) and tabuleiro[3] == " " :     #verificacao1: horizontal, da esquerda para direita
            return 3                                                                                           #verifica se há alguma linha ou coluna faltando apenas uma marcacao para computador para vencer 

    elif (tabuleiro[4] == simboloComputador and tabuleiro[5] == simboloComputador) and tabuleiro[6] == " " :    
            return 6

    elif (tabuleiro[7] == simboloComputador and tabuleiro[8] == simboloComputador) and tabuleiro[9] == " " :  
            return 9                                                                                   
#________________________________________________________________________________________________________________________
    
    elif (tabuleiro[3] == simboloComputador and tabuleiro[2] == simboloComputador) and tabuleiro[1] == " " :     #verificacao2: horizontal, da direita para esquerda
            return 1                                                                                             #verifica se há alguma linha faltando apenas uma marcacao para computador para vencer 

    elif (tabuleiro[6] == simboloComputador and tabuleiro[5] == simboloComputador) and tabuleiro[4] == " " :    
            return 4

    elif (tabuleiro[9] == simboloComputador and tabuleiro[8] == simboloComputador) and tabuleiro[7] == " " :  
            return 7                                                                                   
#________________________________________________________________________________________________________________________
    elif (tabuleiro[1] == simboloComputador and tabuleiro[3] == simboloComputador) and tabuleiro[2] == " " :     #verificacao3: horizontal, alternada
            return 2                                                                                              #verifica se há alguma linha faltando apenas uma marcacao para computador para vencer 

    elif (tabuleiro[4] == simboloComputador and tabuleiro[6] == simboloComputador) and tabuleiro[5] == " " :    
            return 5

    elif (tabuleiro[7] == simboloComputador and tabuleiro[9] == simboloComputador) and tabuleiro[8] == " " :  
            return 8
#________________________________________________________________________________________________________________________
   
    elif (tabuleiro[1] == simboloComputador and tabuleiro[4] == simboloComputador) and tabuleiro[7] == " " :     #verificacao4: vertical, de baixo para cima
            return 7                                                                                             #verifica se há alguma coluna faltando apenas uma marcacao para computador para vencer 

    elif (tabuleiro[2] == simboloComputador and tabuleiro[5] == simboloComputador) and tabuleiro[8] == " " :    
            return 8

    elif (tabuleiro[3] == simboloComputador and tabuleiro[6] == simboloComputador) and tabuleiro[9] == " " :  
            return 9
#________________________________________________________________________________________________________________________

    elif (tabuleiro[7] == simboloComputador and tabuleiro[4] == simboloComputador) and tabuleiro[1] == " " :     #verificacao5: vertical, de cima para baixo
            return 1                                                                                             #verifica se há alguma coluna faltando apenas uma marcacao para computador para vencer 

    elif (tabuleiro[8] == simboloComputador and tabuleiro[5] == simboloComputador) and tabuleiro[2] == " " :    
            return 2

    elif (tabuleiro[9] == simboloComputador and tabuleiro[6] == simboloComputador) and tabuleiro[3] == " " :  
            return 3
#________________________________________________________________________________________________________________________
 
    elif (tabuleiro[1] == simboloComputador and tabuleiro[7] == simboloComputador) and tabuleiro[4] == " " :     #verificacao6: vertical, alternada
            return 4                                                                                             #verifica se há alguma coluna faltando apenas uma marcacao para computador para vencer 

    elif (tabuleiro[2] == simboloComputador and tabuleiro[8] == simboloComputador) and tabuleiro[5] == " " :    
            return 5

    elif (tabuleiro[3] == simboloComputador and tabuleiro[9] == simboloComputador) and tabuleiro[6] == " " :  
            return 6
#________________________________________________________________________________________________________________________

    elif (tabuleiro[1] == simboloComputador and tabuleiro[5] == simboloComputador) and tabuleiro[9] == " " :     #verificacao7: diagonal, de baixo para cima
            return 9                                                                                             #verifica se há alguma diagonal faltando apenas uma marcacao para computador para vencer 

    elif (tabuleiro[3] == simboloComputador and tabuleiro[5] == simboloComputador) and tabuleiro[7] == " " :    
            return 7
#________________________________________________________________________________________________________________________

    elif (tabuleiro[7] == simboloComputador and tabuleiro[5] == simboloComputador) and tabuleiro[3] == " " :     #verificacao8: diagonal, de cima para baixo
            return 3

    elif (tabuleiro[9] == simboloComputador and tabuleiro[5] == simboloComputador) and tabuleiro[1] == " " :    
            return 1
#________________________________________________________________________________________________________________________

    elif (tabuleiro[7] == simboloComputador and tabuleiro[3] == simboloComputador) and tabuleiro[5] == " " :     #verificacao9: diagonais, altermadas
            return 5                                                                                             #verifica se há alguma diagonal faltando apenas uma marcacao para computador para vencer 
        
    elif (tabuleiro[9] == simboloComputador and tabuleiro[1] == simboloComputador) and tabuleiro[5] == " " :    
            return 5
#________________________________________________________________________________________________________________________

    elif ((tabuleiro[1] != " " and tabuleiro[1] != simboloComputador) and (tabuleiro[2] != " " and tabuleiro[2] != simboloComputador)) and tabuleiro[3] == " " :     #verificacao10: horizontal, da esquerda para direita
            return 3                                                                                       #((tabuleiro[x] != " " and tabuleiro[x] != simboloComputador) and (tabuleiro[y] != " " and tabuleiro[y] != simboloComputador))
                                                                                                           #(tabuleiro[x] != " " and tabuleiro[x] != simboloComputador) ==> (tabuleiro[x] = ocupado e tabuleiro[x] = simbolo nao é do computador ), logo o simbulo é do jogador
    elif ((tabuleiro[4] != " " and tabuleiro[4] != simboloComputador) and (tabuleiro[5] != " " and tabuleiro[5] != simboloComputador)) and tabuleiro[6] == " " :
            return 6

    elif ((tabuleiro[7] != " " and tabuleiro[7] != simboloComputador) and (tabuleiro[8] != " " and tabuleiro[8] != simboloComputador)) and tabuleiro[9] == " ":
            return 9                                                        
#________________________________________________________________________________________________________________________

    elif ((tabuleiro[3] != " " and tabuleiro[3] != simboloComputador) and (tabuleiro[2] != " " and tabuleiro[2] != simboloComputador)) and tabuleiro[1] == " ":     #verificacao11: horizontal, da direita para esquerda para 
            return 1                                                                                      #verifica se duas posicoes consecutivas estao ocupadas, se estiver ocupa a terceira.Asim, impedi o oponente de vencer

    elif ((tabuleiro[6] != " " and tabuleiro[6] != simboloComputador) and (tabuleiro[5] != " " and tabuleiro[5] != simboloComputador)) and tabuleiro[4] == " " :
            return 4

    elif ((tabuleiro[9] != " " and tabuleiro[9] != simboloComputador) and (tabuleiro[8] != " " and tabuleiro[8] != simboloComputador)) and tabuleiro[7] == " ":
            return  7                                                     
#________________________________________________________________________________________________________________________

    elif ((tabuleiro[1] != " " and tabuleiro[1] != simboloComputador) and (tabuleiro[4] != " " and tabuleiro[4] != simboloComputador)) and tabuleiro[7] == " ":   #verificacao12: vertical, de baixo para cima
            return 7                                                                                    #verifica se duas posicoes consecutivas estao ocupadas, se estiver ocupa a terceira.Asim, impedi o oponente de vencer
            
    elif ((tabuleiro[2] != " " and tabuleiro[2] != simboloComputador) and (tabuleiro[5] != " " and tabuleiro[5] != simboloComputador)) and tabuleiro[8] == " ":
            return 8

    elif ((tabuleiro[3] != " " and tabuleiro[3] != simboloComputador) and (tabuleiro[6] != " " and tabuleiro[6] != simboloComputador)) and tabuleiro[9] == " ":
            return 9         
#________________________________________________________________________________________________________________________

    elif ((tabuleiro[7] != " " and tabuleiro[7] != simboloComputador) and (tabuleiro[4] != " " and tabuleiro[4] != simboloComputador)) and tabuleiro[1] == " ":   #verificacao13: vertical, de cima para baixo
            return 1                                                                                    #verifica se duas posicoes consecutivas estao ocupadas, se estiver ocupa a terceira.Asim, impedi o oponente de vencer
            
    elif ((tabuleiro[8] != " " and tabuleiro[8] != simboloComputador) and (tabuleiro[5] != " " and tabuleiro[5] != simboloComputador)) and tabuleiro[2] == " ":
            return 2

    elif ((tabuleiro[9] != " " and tabuleiro[9] != simboloComputador) and (tabuleiro[6] != " " and tabuleiro[6] != simboloComputador)) and tabuleiro[3] == " ":
            return 3        
#________________________________________________________________________________________________________________________

    elif ((tabuleiro[1] != " " and tabuleiro[1] != simboloComputador) and (tabuleiro[5] != " " and tabuleiro[5] != simboloComputador)) and tabuleiro[9] == " ":         #verificacao14: diagonal, de baixo para cima
            return 9                                                                                          #verifica se duas posicoes consecutivas estao ocupadas, se estiver ocupa a terceira.Asim, impedi o oponente de vencer
            
    elif ((tabuleiro[3] != " " and tabuleiro[3] != simboloComputador) and (tabuleiro[5] != " " and tabuleiro[5] != simboloComputador)) and tabuleiro[7] == " ":
            return 7
#________________________________________________________________________________________________________________________

    elif ((tabuleiro[7] != " " and tabuleiro[7] != simboloComputador) and (tabuleiro[5] != " " and tabuleiro[5] != simboloComputador)) and tabuleiro[3] == " ":         #verificacao15: diagonal, de cima para baixo
            return 3                                                                                          #verifica se duas posicoes consecutivas estao ocupadas, se estiver ocupa a terceira.Asim, impedi o oponente de vencer
            
    elif ((tabuleiro[9] != " " and tabuleiro[9] != simboloComputador) and (tabuleiro[5] != " " and tabuleiro[5] != simboloComputador)) and tabuleiro[1] == " ":
            return 1  
#________________________________________________________________________________________________________________________

    elif ((tabuleiro[1] != " " and tabuleiro[1] != simboloComputador) and (tabuleiro[9] != " " and tabuleiro[9] != simboloComputador)) and tabuleiro[5] == " ":         #verificacao16: diagonal, alternada
            return 5                                                                                          #verifica se duas posicoes alternadas estao ocupadas, se estiver ocupa a do meio.Asim, impedi o oponente de vencer
            
    elif ((tabuleiro[3] != " " and tabuleiro[3] != simboloComputador) and (tabuleiro[7] != " " and tabuleiro[7] != simboloComputador)) and tabuleiro[5] == " ":
            return 5
#________________________________________________________________________________________________________________________
 
    elif ((tabuleiro[1] != " " and tabuleiro[1] != simboloComputador) and (tabuleiro[3] != " " and tabuleiro[3] != simboloComputador)) and tabuleiro[2] == " " :     #verificacao17: horizontal, posicoes alternadas, da esquerda para direita
            return 2                                                                                       #veirifica se duas posicoes alternadas estão ocupadas, se estiverem: ocupa a posicao entre elas
                
    elif ((tabuleiro[4] != " " and tabuleiro[4] != simboloComputador) and (tabuleiro[6] != " " and tabuleiro[6] != simboloComputador)) and tabuleiro[5] == " " :
            return 5

    elif ((tabuleiro[7] != " " and tabuleiro[7] != simboloComputador) and (tabuleiro[9] != " " and tabuleiro[9] != simboloComputador)) and tabuleiro[8] == " ":
            return 8                                                        
#________________________________________________________________________________________________________________________
    
    elif ((tabuleiro[1] != " " and tabuleiro[1] != simboloComputador) and (tabuleiro[7] != " " and tabuleiro[7] != simboloComputador)) and tabuleiro[4] == " ":   #verificacao18:  vertical, posicoes alternadas, de baixo para cima
            return 4                                                                                    #veirifica se duas posicoes alternadas estão ocupadas, se estiverem: ocupa a posicao entre elas
            
    elif ((tabuleiro[2] != " " and tabuleiro[2] != simboloComputador) and (tabuleiro[8] != " " and tabuleiro[8] != simboloComputador)) and tabuleiro[5] == " ":
            return 5

    elif ((tabuleiro[3] != " " and tabuleiro[3] != simboloComputador) and (tabuleiro[9] != " " and tabuleiro[9] != simboloComputador)) and tabuleiro[6] == " ":
            return  6    
#________________________________________________________________________________________________________________________

    elif tabuleiro[8] == " ":
        return 8
        
    elif tabuleiro[5] == " ":
        return 5

    elif tabuleiro[1] == " ":
        return 1

    elif tabuleiro[3] == " ":
        return 3
    
    elif tabuleiro[7] == " ":
        return 7
    
    elif tabuleiro[9] == " ":
        return 9
    
    elif tabuleiro[2] == " ":
        return 2
    
    elif tabuleiro[4] == " ":
        return 4
    
    elif tabuleiro[6] == " ":
        return 6

def vitoria(tab,simb):
    """
    Verifica se o Jagador ou o Computador venceu, analisando se há uma sequência de 3 letra iguais nas linhas,
    colunas e diagonais.

    Parâmetros:
        tab: lista de tamanho 10 representando o tabuleiro
        simb: letra do jogador da rodada(as rodadas são moderadas pela função jogadas_interc( ))

    Retorno:
    True: se o jogador representado pela letra venceu o jogo
    False: se o jogador representado pela letra não venceu o jogo     
    """
#Verificação horizontal_______________________________________
    if tab[1] == tab[2] == tab[3] == simb:
        return True
    elif tab[4] == tab[5] == tab[6] == simb:
        return True
    elif tab[7] == tab[8] == tab[9] == simb:
        return True
#Verificação vertical_________________________________________
    elif tab[1] == tab[4] == tab[7] == simb:
        return True
    elif tab[2] == tab[5] == tab[8] == simb:
        return True
    elif tab[3] == tab[6] == tab[9] == simb:
        return True
#Verificação Diagonal_________________________________________
    elif tab[1] == tab[5] == tab[9] == simb:
        return True
    elif tab[3] == tab[5] == tab[7] == simb:
        return True
#nao venceu___________________________________________________
    else:
        return False
                    #######################

def empate(vitoria):
    """
    Declara empate(após a nona rodada), caso o jogador ou o computador não tenho vencido antes.

    Parâmetro:
        vitoria: valor(False) obtido com o retorno da função vitoria(), informando que durantes as rodadas
        de 1 a 9 nenhum dos jogadores venceu.
    """
    if vitoria == False:
        print("==>EMPATE")
        encerrar = input("Aperte Enter para encerrar...")

def jogadas_interc(tabuleiro, jogador1, jogador2, simboloJ, simboloC, r=1):
    """
    Alterna as jogadas do Jogador e do Computador(de acordo com a ordem passada pela função main()),
    até que atinja o limite de jogadas(9), verificando a cada jodada sem algum deles venceu,
    caso nenhum vença: ao final da nona jogada é declarado empate.
    Parâmetros:
        tabuleiro: lista de tamanho 10 representando o tabuleiro
        jogador1: primeiro a jogar
        jogador2: segundo ajogar
        simboloJ: letra que representará o jogador(usuário) no tabuleiro
        simboloC: letra que representará o Computador no tabuleiro
        r: contador de rodadas
    """

    if 1 <= r <= 9:
        if r % 2 == 1:                  # o jogo tem 9 rodadas, alternando jogador1 e jogador2. 
            if jogador1 == "Jogador":   # Rodadas ímpares  = jogador1 e rodadas pares = jogador 2
                limpaTela()
                tabuleiroImpressao(tabuleiro)
                posicao = posicao_escolhidaJ()
                if tabuleiro[posicao] == " ":
                    tabuleiro[posicao] = simboloJ
                    if vitoria(tabuleiro[:], simboloJ ) == True:
                        limpaTela()
                        tabuleiroImpressao(tabuleiro)
                        print(" ")
                        print(f"==> O {jogador1} venceu!")
                        encerrar = input("Aperte Enter para encerrar...")
                    else:
                        return jogadas_interc(tabuleiro, jogador1, jogador2, simboloJ, simboloC, r+1)
                else:
                    print("Local já utilizado")
                    novaTentativa = input("Aperte Enter para informar outro...")
                    jogadas_interc(tabuleiro, jogador1, jogador2, simboloJ, simboloC, r)

            elif jogador1 == "Computador":
                posicao = jogadaComputador(tabuleiro[:], simboloC)
                tabuleiro[posicao] = simboloC
                if vitoria(tabuleiro[:], simboloC ) == True:
                        limpaTela()
                        tabuleiroImpressao(tabuleiro)
                        print(" ")
                        print(f"==> O {jogador1} venceu!")
                        encerrar = input("Aperte Enter para encerrar...")
                else:
                    jogadas_interc(tabuleiro, jogador1, jogador2, simboloJ, simboloC, r+1)

        elif r % 2 == 0:
            if jogador2 == "Jogador":
                limpaTela()
                tabuleiroImpressao(tabuleiro)
                posicao = posicao_escolhidaJ()
                if tabuleiro[posicao] == " ":
                    tabuleiro[posicao] = simboloJ
                    if vitoria(tabuleiro[:], simboloJ ) == True:
                        limpaTela()
                        tabuleiroImpressao(tabuleiro)
                        print(" ")
                        print(f"==> O {jogador2} venceu!")
                        encerrar = input("Aperte Enter para encerrar...")
                    else:
                        return jogadas_interc(tabuleiro, jogador1, jogador2, simboloJ, simboloC, r+1)
                else:
                    print("Local já utilizado")
                    novaTentativa = input("Aperte Enter para informar outro...")
                    jogadas_interc(tabuleiro, jogador1, jogador2, simboloJ, simboloC, r)

            elif jogador2 == "Computador":
                posicao = jogadaComputador(tabuleiro[:], simboloC)
                tabuleiro[posicao] = simboloC
                if vitoria(tabuleiro[:], simboloC ) == True:
                        limpaTela()
                        tabuleiroImpressao(tabuleiro)
                        print(" ")
                        print(f"==> O {jogador2} venceu!")
                        encerrar = input("Aperte Enter para encerrar...")
                else:
                    jogadas_interc(tabuleiro, jogador1, jogador2, simboloJ, simboloC, r+1)
    else:
        limpaTela()
        tabuleiroImpressao(tabuleiro)
        print(" ")
        empate(vitoria(tabuleiro[:], simboloC ))
 
    


def main():
    """
    Dá início a execução do do cógigo:
    limpa tela;
    imprime o numero de matricula, chamando (dentro da função print()) a função getMatricula();
    imprime o nome, chamando (dentro da função print()) a função getNome(); 
    define o tabuleiro(lista com índice 10, sendo o índice [0] ignorado durante todo código);
    solicita ao jogador a escolha da letra(X ou O) que usará para jogar, a letra restante é atribuída ao computador;
    sorteia (por meio da função sorteio()) a ordem em que o jogador e o computador devem jogar;
    dá início ao jogo chamando a função jogadas_interc() e passando o tabuleiro, a ordem em que os jogadorem jogarão,
    e as respectivas letras; 
    """
    limpaTela()
    print(getMatricula())
    print(getNome())
    
    tabuleiro = [" "]*10

    print(" ")
    simboloJ, simboloC = defSimbulo( )
    j1, j2 = sorteio()

    jogadas_interc(tabuleiro, j1, j2, simboloJ, simboloC)
    

    


if __name__ == "__main__":
    main()