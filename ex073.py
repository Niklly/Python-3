''' Crie uma tupla com os 20 primeiros colocados da Tabela do *CAMPEONATO BRASILEIRO DE FUTEBOL*, na ordem de colocação. Depois mostre:

A) Apenas os 5 primeiros colocados
B) Os últimos 4 colocados da tabela
C) Uma lista com os times em ordem alfabética
C) Em que posição na tabela está o time da CHAPECOENSE.

'''

times_brasileirao = ('Corinthians','Palmeiras','Santos','Grêmio','Cruzeiro','Flamengo','Vasco','Chapecoense','Atlético','Botafogo','Atlético-PR','Bahia','São Paulo','Fluminense','Sport Recife', 'Ec Vitoria','Coritiba', 'Avaí','Ponte Preta','Atlético-GO')
posicao_chapecoense = times_brasileirao.index('Chapecoense')

print(f'Lista de times do Brasileirão:\033[32m{times_brasileirao}\033[m')
print('=='*65)
print(f'Os 5 primeiros classificados: \033[33m{times_brasileirao[0:5]}\033[m')
print('=='*65)
print(f'Os últimos 4 colocados: \033[34m{times_brasileirao[-4:]}\033[m')
print('=='*65)
print(f'Lista de time em ordem alfábetica: \033[31m{sorted(times_brasileirao)}\033[m')
print('=='*65)
print('Time Chapecoense:\033[36m{}° posição\033[m'.format(posicao_chapecoense+1))


