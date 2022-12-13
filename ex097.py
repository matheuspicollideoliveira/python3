def escreva(msg):
    print((len(msg)+4) * '-')
    print(f'  {msg}')
    print((len(msg)+4) * '-')


while True:
    escreva(str(input('Mensagem:')))
    while True:
        resp = str(input('Quer escrever outra mensagem? [S/N]')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO. Digite S ou N.')
    print(15 * '=-')
    if resp in 'N':
        break
print('Obrigado por utilizar o nosso programa!')
