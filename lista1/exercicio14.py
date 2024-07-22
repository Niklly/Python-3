#corredor 1 
print(f"*Tempo do Corredor 1*")
horas1 = int(input("-> Quantas horas:"))
minutos1 = int(input("-> Quantos minutos:"))
segundos1 = int(input("-> Quantos segundos:"))

#corredor 2

print(f"*Tempo do Corredor 2*")
horas2 = int(input("-> Quantas horas:"))
minutos2 = int(input("-> Quantos minutos:"))
segundos2 = int(input("-> Quantos segundos:"))


#conversão do corredor1

# 1 hora = 60 minutos = 3600 segundos
# 1/60 hora  =  1 minuto = 60 segundos

hor_seg1 = (60 * horas1 * 60)
min_seg1 = (minutos1 * 60)
seg_total = (hor_seg1 + min_seg1 + segundos1)


hor_seg2= (60 * horas2 * 60)
min_seg2 = (minutos2 * 60)
seg_total2 = (hor_seg2 + min_seg2 + segundos2)



if seg_total > seg_total2:
    diferenca = (seg_total - seg_total2)
    resto_hora = diferenca % 3600
    resto_minuto = resto_hora % 60
    conversao_minuto = int((resto_hora/3600) *60)
    conversao_hora = int(diferenca/3600)
    print("Vencedor: corredor 1")
    print("Diferença:", conversao_hora, "horas", conversao_minuto, "minutos", resto_minuto, "segundos"  )


elif seg_total2 > seg_total:
    diferenca2 = (seg_total2 - seg_total)
    resto_hora = diferenca2 % 3600
    resto_minuto = resto_hora % 60
    conversao_minuto = int((resto_hora/3600) *60)
    conversao_hora = int(diferenca2/3600)
    print("Vencedor: corredor 2")
    print("Diferença:", conversao_hora, "horas", conversao_minuto, "minutos", resto_minuto, "segundos"  )
