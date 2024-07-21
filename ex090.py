aluno = dict()

aluno['nome'] = str(input("Nome: "))
aluno['media'] = float(input(f"Média de {aluno['nome']}: "))

if aluno['media'] >= 7:
   aluno['situação'] = 'Aprovado'
elif 5 <= aluno['media'] < 7:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

for k,v in aluno.items():
    print(f"- {k} é igual a {v}.")

'''
print("=*"*25)
print(f"- nome é igual a {aluno['nome']}")
print(f"- média é igual a {aluno['media']}")
print(f"- situação é igual a {aluno['situação']}")
'''