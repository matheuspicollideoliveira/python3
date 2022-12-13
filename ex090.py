aluno = dict()
aluno['nome'] = str(input('Nome:'))
aluno['média'] = float(input(f'Média de {aluno["nome"]}:'))
if aluno['média'] >= 7:
    aluno['situação'] = '\33[32mAprovado!'
elif 5 <= aluno['média'] < 7:
    aluno['situação'] = '\33[33mRecuperação!'
else:
    aluno['situação'] = '\33[31mReprovado!'
print(30 * '-')
for k, v in aluno.items():
    print(f' - {k} é igual a {v}')
