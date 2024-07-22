def converter(s):

    resto_hora = s % 3600
    resto_min = resto_hora % 60

    conversao_min = int((resto_hora/60))
    conversao_hora = int(s/3600)
    
    print(conversao_hora,"horas", conversao_min,"minutos", resto_min,"segundos")
    print(resto_hora)
    
def main():
    s = int(input(f"Digite a quantidade de segundos: "))
    converter(s)

main()