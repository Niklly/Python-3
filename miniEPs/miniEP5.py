# n é a quantidade de candidatos participando
# n_v é a quantidade de votos computados 

def candidatos(n_c,L, i=0):

    if i < n_c:
        nome_candidatos = input("Escreva o nome do candidato(a):")
        L[i] = nome_candidatos
        return candidatos(n_c,L,i+1)
    return L
    
def votos_candidatos(Votos,n_v,i=0):

    if i < n_v:
        voto_eleitor = int(input("Digite o voto para seu candidato:"))
        if voto_eleitor > n_v:
            Votos[-1] += 1
        else:
            Votos[voto_eleitor] += 1
        return votos_candidatos(Votos, n_v, i+1)
    else:
        return Votos



def main():
    n_c = int(input("quantos participantes temos?"))
    ListaCandidatos = [''] * (1+n_c)
    ListaCandidatos[0] = "Branco"
    ListaCandidatos[-1] = "Nulo"
    ListaCandidatos = candidatos(n_c,ListaCandidatos)
    n_v = int(input("quantos votos temos?"))
    Votos = [0] * (1 + n_c)
    Votos = votos_candidatos(Votos, n_v)
   
main()