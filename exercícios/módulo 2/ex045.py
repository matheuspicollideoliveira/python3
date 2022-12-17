from random import choice
from time import sleep
print('Vamos jogar Jokenpo?')
print('''Escolha uma das opções abaixo:
\33[31m- pedra\33[m
\33[32m- papel\33[m
\33[33m- tesoura\33[m''')
pedra = 'pedra'
papel = 'papel'
tesoura = 'tesoura'
lista = [pedra, papel, tesoura]
escolha = choice(lista)
opcao = str(input('Digite a opção que escolheu:'))
print('\33[0:31mJO\33[m')
sleep(1)
print('\33[32mKEN\33[m')
sleep(1)
print('\33[33mPO\33[m')
sleep(1)
print('-' * 70)
if escolha == opcao:
    print(f'\33[36mEu escolhi {escolha} e você também, então empatamos\33[m!')
elif escolha == papel and opcao == tesoura:
    print(f'Eu escolhi {escolha} e você escolheu tesoura, Parabéns você me \33[0:32mvenceu!\33[m')
elif escolha == tesoura and opcao == papel:
    print(f'Eu escolhi {escolha} e você escolheu papel, você \33[0:31mperdeu!\33[m')
elif escolha == pedra and opcao == papel:
    print(f'Eu escolhi {escolha} e você escolheu papel, Parabéns você me \33[0:32mvenceu!\33[m')
elif escolha == papel and opcao == pedra:
    print(f'Eu escolhi {escolha} e você escolheu pedra, você \33[0:31mperdeu!\33[m')
elif escolha == tesoura and opcao == pedra:
    print(f'Eu escolhi {escolha} e você escolheu pedra, Parabéns você me \33[0:32mvenceu!\33[m')
elif escolha == pedra and opcao == tesoura:
    print(f'Eu escolhi {escolha} e você escolheu tesoura, você \33[0:31mperdeu!\33[m')
else:
    print('\33[1:31mNÃO TEMOS ESSA OPÇÃO!\33[m')
print('-' * 70)