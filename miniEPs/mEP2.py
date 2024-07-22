# ENTRADA
Peso = float(input())

Idade = int(input())
if Idade == 16 or Idade == 17:
    Documento_autorizacao  = str(input())
    if Documento_autorizacao == "s" or Documento_autorizacao == "S":
        Documento = True 
    else:
        Documento = False   
        
Boa_saude = str(input())
Uso_de_drogas = str(input())

Primeira_doacao = str(input())
if Primeira_doacao == "N":
    Meses_ultima_doacao = int(input())
    Doacao_entre_12m = int(input())
    
Sexo_biologico = str(input())
if Sexo_biologico == "F":
    Gravidez = str(input())
    Amamentando = str(input()) 
    if Amamentando == "S":
        Meses_do_bebe = int(input()) 
    
# SAÍDA

print("Peso:",Peso)
print("Idade:",Idade)

if Idade == 16 or Idade == 17:
    print("Documento de autorizacao:",Documento_autorizacao)

print("Boa saude:",Boa_saude)
print("Uso de drogas injetaveis:",Uso_de_drogas)
print("Primeira doacao:",Primeira_doacao)

if Primeira_doacao == "N":
    print("Meses desde ultima doacao:",Meses_ultima_doacao)
    print("Doacoes nos ultimos 12 meses:",Doacao_entre_12m)

print("Sexo biologico:",Sexo_biologico)
    
if Sexo_biologico == "F":
    print("Gravidez:",Gravidez)
    print("Amamentando:",Amamentando) 
    if Amamentando == "S":
        print("Meses bebe:",Meses_do_bebe)

# IMPEDIMENTOS

Impedimentos = 0

if Peso < 50.00:
    print("Impedimento: abaixo do peso minimo.")
    Impedimentos +=1

if Idade < 16:
    print("Impedimento: menor de 16 anos.")
    Impedimentos +=1

elif (Idade == 16 or Idade == 17) and (Documento == False) :
    print("Impedimento: menor de 18 anos, sem consentimento dos responsaveis.")
    Impedimentos +=1

elif  (Idade > 60.0 and Idade <= 69):
    print("Impedimento: maior de 60 anos, primeira doacao.") 
    Impedimentos +=1  

elif (Idade > 69):
    print("Impedimento: maior de 69 anos.")
    Impedimentos +=1

if Boa_saude == ("N"):
    print("Impedimento: nao esta em boa saude.")
    Impedimentos +=1

if Uso_de_drogas == ("S"):
    print("Impedimento: uso de drogas injetaveis.")
    Impedimentos +=1

if Primeira_doacao == "N":
    if Sexo_biologico == ("F") and Meses_ultima_doacao <= 3:
        print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado.")
        Impedimentos +=1

    if Sexo_biologico == ("F") and Doacao_entre_12m >= 3:
        print("Impedimento: numero maximo de doacoes anuais foi atingido.")
        Impedimentos +=1

    elif Sexo_biologico == ("M") and Meses_ultima_doacao <= 2:
        print("Impedimento: intervalo minimo entre as doacoes nao foi respeitado.")
        Impedimentos +=1

    if Sexo_biologico == ("M") and Doacao_entre_12m >= 4:
        print("Impedimento: numero maximo de doacoes anuais foi atingido.")
        Impedimentos +=1

if Sexo_biologico == ("F"):    
    if Gravidez == ("S"):
        print("Impedimento: gravidez.")
        Impedimentos +=1

    if Amamentando == ("S"):
        if Meses_do_bebe < 12:
            print("Impedimento: amamentacao.")
            Impedimentos +=1
        
if Impedimentos == 0:
    print("Procure um hemocentro.")





