numeros = ('zero','um','dois','três','quatro',
           'cinco','seis','sete','oito','nove',
           'dez','onze','doze','treze','quatorze',
           'quinze','dezesseis','dezessete','dezoito',
           'dezenove','vinte')
while True:
    num = int(input('Digite um número entre 0 e 20:'))
    while num < 0 or num > 20:
        num = int(input('Tente novamente. Digite um número entre 0 e 20:'))
    print(f'Você digitou o número {numeros[num]}!')
    r = str(input('Quer continuar? [S/N]')).strip().upper()[0]
    if r in 'Nn':
        break
print('Obrigado por utilizar nosso programa!')


