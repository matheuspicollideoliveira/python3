import random
aluno1 = str(input('Primeiro aluno:'))
aluno2 = str(input('Segundo aluno:'))
aluno3 = str(input('Terceiro Aluno:'))
aluno4 = str(input('Qaurto aluno:'))
list = [aluno1, aluno2, aluno3, aluno4]
sorteio = random.choice(list)
print(f'O escolhido para apagar o quadro é {sorteio}')
