
# 1 hora = 60 minutos = 3600 segundos
# 1 minuto = 60 segundos 
# 3672 segundos = 1 hora = 0,12 horas * 60 = 1 minuto = 0,2 minutos * 60 = 12 segundos


tempo = int(input("Digite o tempo gasto em segundos pelo programados:"))

resto_hora = tempo % 3600
resto_minuto = resto_hora % 60

conversao_minuto = int((resto_hora/3600) *60)
conversao_hora = int(tempo/3600)

print("O tempo gasto pelo programador foi de", conversao_hora,":",conversao_minuto,":", resto_minuto)


