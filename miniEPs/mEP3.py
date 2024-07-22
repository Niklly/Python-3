def notacion(x):
    if x == 0:
        y = '00'
    elif x < 10:
        y = '0'+str(x)
    else:
        y = str(x)
    return y 

def horas_min (x):
    horas = notacion(abs(x)//60)+'h'
    minutos = notacion(abs(x) % 60)+'min'
    return [horas,minutos]


def corredor(sexo, idade,t_n):

    if sexo == "F" or sexo == "f":
        if idade >= 18 and idade <= 34:
            t_n = 210
            return(t_n)
        elif idade >= 35 and idade <= 39:
            t_n = 215
            return(t_n)
        elif idade >= 40 and idade <= 44:
            t_n = 220
            return(t_n)
        elif idade >= 45 and idade <= 49:
            t_n = 230
            return(t_n)
        elif idade >= 50 and idade <= 54:
            t_n = 235
            return(t_n)
        elif idade >= 55 and idade <= 59:
            t_n = 245
            return(t_n)
        elif idade >= 60 and idade <= 64:
            t_n = 260
            return(t_n)
        elif idade >= 65 and idade <= 69:
            t_n = 275
            return(t_n)
        elif idade >= 70 and idade <= 74:
            t_n = 290
            return(t_n)
        elif idade >=75 and idade <=79:
            t_n = 305
            return(t_n)
        elif idade >=80:
            t_n = 320
            return (t_n)




def saida(sexo,tempo_necessario,tempo_corredor,tempo_abaixo,t):
    if sexo == "m" or sexo == "M":
        print("Tempo do corredor: "+tempo_corredor[0]+" "+tempo_corredor[1])
        print("Tempo necessario: "+tempo_necessario[0]+" "+tempo_necessario[1])
        if t < 0:
            print("Conseguiu indice? NAO")
            print("O corredor correu "+tempo_abaixo[0]+" "+tempo_abaixo[1]+" acima do indice")
        else:
            print("Conseguiu indice? SIM")
            print("O corredor correu "+tempo_abaixo[0]+" "+tempo_abaixo[1]+" abaixo do indice")

    else:
        print("Tempo do corredora: "+tempo_corredor[0]+" "+tempo_corredor[1])
        print("Tempo necessario: "+tempo_necessario[0]+" "+tempo_necessario[1])
        if t < 0:
            print("Conseguiu indice? NAO")
            print("O corredor correu "+tempo_abaixo[0]+" "+tempo_abaixo[1]+" acima do indice")
        else:
            print("Conseguiu indice? SIM")
            print("A correda correu "+tempo_abaixo[0]+" "+tempo_abaixo[1]+" abaixo do indice")



def main():
    tempo_corredor =  int(input())
    idade = int(input())
    sexo = str(input())
    t_n = corredor(idade,sexo, tempo_corredor)
    tempo_corredor= horas_min(tempo_corredor)
    tempo_necessario = horas_min(t_n)
    t = t_n - tempo_corredor
    tempo_abaixo = horas_min(t)


main()