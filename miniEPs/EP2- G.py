import random
from os import system, name 

# RED     = '\033[31m'
# GREEN   = '\033[32m'
# YELLOW  = '\033[33m'
# BLUE    = '\033[34m'
# VIOLET  = '\033[35m'
# WHITE   = '\033[37m'

def EscolhaSimbolo():
    try:
        simbJogador = input("Você quer ser 'X' ou 'O'? ")
    except:
        print("Simbolo inválido!")
        return EscolhaSimbolo()
    if simbJogador == "X" or simbJogador == "x":
        simbJogador = "X"
        sComp = "O"
        return simbJogador, sComp
    elif simbJogador == "O" or simbJogador == "o":
        simbJogador = "O"
        sComp = "X"
        return simbJogador, sComp
    else:
        print("Símbolo inválido!")
        return EscolhaSimbolo()
    


    
def ImprimeTabuleiro(tabuleiro_Principal):
    print(f" {tabuleiro_Principal[7]} | {tabuleiro_Principal[8]} | {tabuleiro_Principal[9]} ")
    print(f"---+---+---")
    print(f" {tabuleiro_Principal[4]} | {tabuleiro_Principal[5]} | {tabuleiro_Principal[6]} ")
    print(f"---+---+---")
    print(f" {tabuleiro_Principal[1]} | {tabuleiro_Principal[2]} | {tabuleiro_Principal[3]} ")

def JogaPrimeiro():
    primeiro = random.choice([0,1])
    return primeiro

def limpaTela(): 
	if name == 'nt': 
		system('cls') 
	else: 
		system('clear') 

def VerificaVencedor(tabuleiro, simboloJogador):
    # LINHA 1
    if (tabuleiro[1] == "X" and tabuleiro[2] == "X" and tabuleiro[3] == "X") or (tabuleiro[1] == "O" and tabuleiro[2] == "O" and tabuleiro[3] == "O"):
        if tabuleiro[1] == simboloJogador:
            ImprimeTabuleiro(tabuleiro)
            print()
            print("PARABÉNS, VOCÊ GANHOU!")
            print()
            return True
        else:
            ImprimeTabuleiro(tabuleiro)
            print()
            print("O COMPUTADOR GANHOU!")
            print()
            return True
    # LINHA 2
    elif (tabuleiro[4] == "X" and tabuleiro[5] == "X" and tabuleiro[6] == "X") or (tabuleiro[4] == "O" and tabuleiro[5] == "O" and tabuleiro[6] == "O"):
        if tabuleiro[4] == simboloJogador:
            ImprimeTabuleiro(tabuleiro)
            print()
            print("PARABÉNS, VOCÊ GANHOU!")
            print()
            return True
        else:
            ImprimeTabuleiro(tabuleiro)
            print()
            print("O COMPUTADOR GANHOU!")
            print()
            return True
    # LINHA 3
    elif (tabuleiro[7] == "X" and tabuleiro[8] == "X" and tabuleiro[9] == "X") or (tabuleiro[7] == "O" and tabuleiro[8] == "O" and tabuleiro[9] == "O"):
        if tabuleiro[7] == simboloJogador:
            ImprimeTabuleiro(tabuleiro)
            print()
            print("PARABÉNS, VOCÊ GANHOU!")
            print()
            return True
        else:
            ImprimeTabuleiro(tabuleiro)
            print()
            print("O COMPUTADOR GANHOU!")
            print()
            return True
    # COLUNA 1
    elif (tabuleiro[1] == "X" and tabuleiro[4] == "X" and tabuleiro[7] == "X") or (tabuleiro[1] == "O" and tabuleiro[4] == "O" and tabuleiro[7] == "O"):
        if tabuleiro[1] == simboloJogador:
            ImprimeTabuleiro(tabuleiro)
            print()
            print("PARABÉNS, VOCÊ GANHOU!")
            print()
            return True
        else:
            ImprimeTabuleiro(tabuleiro)
            print()
            print("O COMPUTADOR GANHOU!")
            print()
            return True
    # COLUNA 2
    elif (tabuleiro[2] == "X" and tabuleiro[5] == "X" and tabuleiro[8] == "X") or (tabuleiro[2] == "O" and tabuleiro[5] == "O" and tabuleiro[8] == "O"):
        if tabuleiro[2] == simboloJogador:
            ImprimeTabuleiro(tabuleiro)
            print()
            print("PARABÉNS, VOCÊ GANHOU!")
            print()
            return True
        else:
            ImprimeTabuleiro(tabuleiro)
            print()
            print("O COMPUTADOR GANHOU!")
            print()
            return True
    # COLUNA 3
    elif (tabuleiro[3] == "X" and tabuleiro[6] == "X" and tabuleiro[9] == "X") or (tabuleiro[3] == "O" and tabuleiro[6] == "O" and tabuleiro[9] == "O"):
        if tabuleiro[3] == simboloJogador:
            ImprimeTabuleiro(tabuleiro)
            print()
            print("PARABÉNS, VOCÊ GANHOU!")
            print()
            return True
        else:
            ImprimeTabuleiro(tabuleiro)
            print()
            print("O COMPUTADOR GANHOU!")
            print()
            return True
    # DIAGONAL 1
    elif (tabuleiro[1] == "X" and tabuleiro[5] == "X" and tabuleiro[9] == "X") or (tabuleiro[1] == "O" and tabuleiro[5] == "O" and tabuleiro[9] == "O"):
        if tabuleiro[1] == simboloJogador:
            ImprimeTabuleiro(tabuleiro)
            print()
            print("PARABÉNS, VOCÊ GANHOU!")
            print()
            return True
        else:
            ImprimeTabuleiro(tabuleiro)
            print()
            print("O COMPUTADOR GANHOU!")
            print()
            return True
    # DIAGONAL 2
    elif (tabuleiro[3] == "X" and tabuleiro[5] == "X" and tabuleiro[7] == "X") or (tabuleiro[3] == "O" and tabuleiro[5] == "O" and tabuleiro[7] == "O"):
        if tabuleiro[3] == simboloJogador:
            ImprimeTabuleiro(tabuleiro)
            print()
            print("PARABÉNS, VOCÊ GANHOU!")
            print()
            return True
        else:
            ImprimeTabuleiro(tabuleiro)
            print()
            print("O COMPUTADOR GANHOU!")
            print()
            return True
    else:
        return False
    
def Jogadas(sJogador, sComp, tabuleiro, contJogadas = 0, quemJoga = 0):
    quemJoga = JogaPrimeiro() if contJogadas == 0 else quemJoga
    if VerificaVencedor(tabuleiro, sJogador) == True:
        exit()
    if contJogadas < 9:
        if quemJoga == 1:
            if contJogadas == 0:
                print("O computador começa.")
            jComp = jogadaComputador(tabuleiro, sComp)
            tabuleiro = tabuleiro[:]
            tabuleiro[jComp] = sComp
            return Jogadas(sJogador, sComp, tabuleiro, contJogadas + 1, quemJoga = 0)
        else:
            if contJogadas == 0:
                print("Você começa.")
            ImprimeTabuleiro(tabuleiro)
            try:
                p = int(input("Qual posição deseja marcar (1-9): "))
            except:
                print("Valor inválido. Você deve digitar um número inteiro entre 1 e 9.")
                return Jogadas(sJogador, sComp, tabuleiro, contJogadas, quemJoga = 0)
            if (p < 1) or (p > 9):
                print("Valor inválido. Você deve digitar um número inteiro entre 1 e 9.")
                return Jogadas(sJogador, sComp, tabuleiro, contJogadas, quemJoga = 0)
            tabuleiro = tabuleiro[:]
            tabuleiro[p] = sJogador
            return Jogadas(sJogador, sComp, tabuleiro, contJogadas + 1, quemJoga = 1)
    else:
        ImprimeTabuleiro(tabuleiro)
        print()
        print("EMPATE!")
        print()
def jogadaComputador(tabuleiro, simboloComputador, i = 0, Posiçao_Livre = [], Posiçao_Jogada = []):
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
    Explique aqui, de forma resumida, a sua estratégia usada para o computador vencer o jogador
    """
    primeiro = JogaPrimeiro()
    simboloJogador = "X" if simboloComputador == "O" else "O"
    if i <= 9:
        if tabuleiro[i] == " ":
            Posiçao_Livre = Posiçao_Livre[:] + [i]
            return jogadaComputador(tabuleiro, simboloComputador, i + 1, Posiçao_Livre, Posiçao_Jogada)
        else:
            Posiçao_Jogada = Posiçao_Jogada[:] + [i]
            return jogadaComputador(tabuleiro, simboloComputador, i + 1, Posiçao_Livre, Posiçao_Jogada)
            
    if  (len(tabuleiro) == len(Posiçao_Livre)) or len(Posiçao_Livre) == 9:
        return random.choice(Posiçao_Livre[1:])
    if (primeiro == 1) and (len(Posiçao_Livre) == 8):
        return random.choice(Posiçao_Livre[1:])
    elif (primeiro == 0) and (len(Posiçao_Livre)) == 8:
        return random.choice(Posiçao_Livre[1:])
    # LINHA 1
    if ((tabuleiro[1] == simboloJogador) and (tabuleiro[2] == simboloJogador) and tabuleiro[3] == " ") or ((tabuleiro[1] == simboloComputador) and (tabuleiro[2]== simboloComputador) and tabuleiro[3] == " "):
        return 3
    if ((tabuleiro[1] == simboloJogador) and (tabuleiro[3] == simboloJogador) and tabuleiro[2] == " ") or ((tabuleiro[1] == simboloComputador) and (tabuleiro[3]== simboloComputador) and tabuleiro[2] == " "):
        return 2
    if ((tabuleiro[2] == simboloJogador) and (tabuleiro[3] == simboloJogador) and tabuleiro[1] == " ") or ((tabuleiro[2] == simboloComputador) and (tabuleiro[3]== simboloComputador) and tabuleiro[1] == " "):
        return 1
    # LINHA 2
    if ((tabuleiro[4] == simboloJogador) and (tabuleiro[5] == simboloJogador) and tabuleiro[6] == " ") or ((tabuleiro[4] == simboloComputador) and (tabuleiro[5]== simboloComputador) and tabuleiro[6] == " "):
        return 6
    if ((tabuleiro[4] == simboloJogador) and (tabuleiro[6] == simboloJogador) and tabuleiro[5] == " ") or ((tabuleiro[4] == simboloComputador) and (tabuleiro[6]== simboloComputador) and tabuleiro[5] == " "):
        return 5
    if ((tabuleiro[5] == simboloJogador) and (tabuleiro[6] == simboloJogador) and tabuleiro[4] == " ") or ((tabuleiro[5] == simboloComputador) and (tabuleiro[6]== simboloComputador) and tabuleiro[4] == " "):
        return 4
    # LINHA 3
    if ((tabuleiro[7] == simboloJogador) and (tabuleiro[8] == simboloJogador) and tabuleiro[9] == " ") or ((tabuleiro[7] == simboloComputador) and (tabuleiro[8]== simboloComputador) and tabuleiro[9] == " "):
        return 9
    if ((tabuleiro[7] == simboloJogador) and (tabuleiro[9] == simboloJogador) and tabuleiro[8] == " ") or ((tabuleiro[7] == simboloComputador) and (tabuleiro[9]== simboloComputador) and tabuleiro[8] == " "):
        return 8
    if ((tabuleiro[8] == simboloJogador) and (tabuleiro[9] == simboloJogador) and tabuleiro[7] == " ") or ((tabuleiro[8] == simboloComputador) and (tabuleiro[9]== simboloComputador) and tabuleiro[7] == " "):
        return 7
    # COLUNA 1
    if ((tabuleiro[1] == simboloJogador) and (tabuleiro[4] == simboloJogador) and tabuleiro[7] == " ") or ((tabuleiro[1] == simboloComputador) and (tabuleiro[4]== simboloComputador) and tabuleiro[7] == " "):
        return 7
    if ((tabuleiro[1] == simboloJogador) and (tabuleiro[7] == simboloJogador) and tabuleiro[4] == " ") or ((tabuleiro[1] == simboloComputador) and (tabuleiro[7]== simboloComputador) and tabuleiro[4] == " "):
        return 4
    if ((tabuleiro[4] == simboloJogador) and (tabuleiro[7] == simboloJogador) and tabuleiro[1] == " ") or ((tabuleiro[4] == simboloComputador) and (tabuleiro[7]== simboloComputador) and tabuleiro[1] == " "):
        return 1
    # COLUNA 2
    if ((tabuleiro[2] == simboloJogador) and (tabuleiro[5] == simboloJogador) and tabuleiro[8] == " ") or ((tabuleiro[2] == simboloComputador) and (tabuleiro[5]== simboloComputador) and tabuleiro[8] == " "):
        return 8
    if ((tabuleiro[2] == simboloJogador) and (tabuleiro[8] == simboloJogador) and tabuleiro[5] == " ") or ((tabuleiro[2] == simboloComputador) and (tabuleiro[8]== simboloComputador) and tabuleiro[5] == " "):
        return 5
    if ((tabuleiro[5] == simboloJogador) and (tabuleiro[8] == simboloJogador) and tabuleiro[2] == " ") or ((tabuleiro[5] == simboloComputador) and (tabuleiro[8]== simboloComputador) and tabuleiro[2] == " "):
        return 2
    # COLUNA 3
    if ((tabuleiro[3] == simboloJogador) and (tabuleiro[6] == simboloJogador) and tabuleiro[9] == " ") or ((tabuleiro[3] == simboloComputador) and (tabuleiro[6]== simboloComputador) and tabuleiro[9] == " "):
        return 9
    if ((tabuleiro[3] == simboloJogador) and (tabuleiro[9] == simboloJogador) and tabuleiro[6] == " ") or ((tabuleiro[3] == simboloComputador) and (tabuleiro[9]== simboloComputador) and tabuleiro[6] == " "):
        return 6
    if ((tabuleiro[6] == simboloJogador) and (tabuleiro[9] == simboloJogador) and tabuleiro[3] == " ") or ((tabuleiro[6] == simboloComputador) and (tabuleiro[9]== simboloComputador) and tabuleiro[3] == " "):
        return 3
    # DIAGONAL 1
    if ((tabuleiro[1] == simboloJogador) and (tabuleiro[5] == simboloJogador) and tabuleiro[9] == " ") or ((tabuleiro[1] == simboloComputador) and (tabuleiro[5]== simboloComputador) and tabuleiro[9] == " "):
        return 9
    if ((tabuleiro[1] == simboloJogador) and (tabuleiro[9] == simboloJogador) and tabuleiro[5] == " ") or ((tabuleiro[1] == simboloComputador) and (tabuleiro[9]== simboloComputador) and tabuleiro[5] == " "):
        return 5
    if ((tabuleiro[5] == simboloJogador) and (tabuleiro[9] == simboloJogador) and tabuleiro[1] == " ") or ((tabuleiro[5] == simboloComputador) and (tabuleiro[9]== simboloComputador) and tabuleiro[1] == " "):
        return 1
    # DIAGONAL 2
    if ((tabuleiro[3] == simboloJogador) and (tabuleiro[5] == simboloJogador) and tabuleiro[7] == " ") or ((tabuleiro[3] == simboloComputador) and (tabuleiro[5]== simboloComputador) and tabuleiro[7] == " "):
        return 7
    if ((tabuleiro[3] == simboloJogador) and (tabuleiro[7] == simboloJogador) and tabuleiro[5] == " ") or ((tabuleiro[3] == simboloComputador) and (tabuleiro[7]== simboloComputador) and tabuleiro[5] == " "):
        return 5
    if ((tabuleiro[5] == simboloJogador) and (tabuleiro[7] == simboloJogador) and tabuleiro[3] == " ") or ((tabuleiro[5] == simboloComputador) and (tabuleiro[7]== simboloComputador) and tabuleiro[3] == " "):
        return 3
    else:
        return random.choice(Posiçao_Livre[1:])
    
    
    
    

def main():
    limpaTela()
    #Você pode, se quiser, comentar os dois prints abaixo:
    #print(getNome())
    #print(getMatricula())
    tabuleiro_Principal = [" "," "," "," ", " ", " ", " ", " ", " ", " "]
    SimbJogador, sComp = EscolhaSimbolo()
    Jogadas(SimbJogador, sComp, tabuleiro_Principal)



main()