from time import sleep
dados = []
alunos = []
while True:
    nome = str(input('Nome: '))
    dados.append(nome)
    notaum = float(input('Nota 1: '))
    dados.append(notaum)
    notadois = float(input('Nota 2: '))
    dados.append(notadois)

    alunos.append(dados[:])
    dados.clear()

    continuar = str(input('Quer continuar [S/N]: '))
    if continuar in 'Nn':
        break
print('=-'*20)
print('N°',' '*1, 'Nome',' '*2,'Média')
print('=='*20)
for i, pessoa in enumerate(alunos):
    media = (pessoa[1]+pessoa[2])/2
    print(i, end='')
    print(f' '*3,pessoa[0],end=' ')
    print(f'  {media:^.2f}')

print('=-' * 20)
boletim = int(input(f'Mostrar notas de qual aluno? (999 interrompe):  '))

while boletim != 999:
    for i, pessoa in enumerate(alunos):
        print(f'As notas de {alunos[boletim][0]} foram: [{alunos[boletim][1]}, {alunos[boletim][2]}]')
        print('=-' * 20)
        boletim = int(input(f'Você gostaria de saber o boletim de qual aluno? [999 para interromper] '))
    if boletim == 999:
        break

print('Finalizando...')
sleep(2)
print('<<<< VOLTE SEMPRE >>>>')

