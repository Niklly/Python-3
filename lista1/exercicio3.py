t_total = int(input("Digite o tempo total gasto na corrida (em min):"))
d_percorrida = int(input("Digite a distância percorrida (em km):"))
ritmo = float(t_total / d_percorrida)


print(f"Ritmo medio do corredor: ",ritmo,"min/km")