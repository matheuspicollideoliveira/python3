from time import sleep
c =('\33[m',
    '\33[0;30;41m',
    '\33[0;30;42m',
    '\33[0;30;43m',
    '\33[0;30;44m',
    '\33[0;30;45m',
    '\33[7;30m')


def ajuda(com):
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[3], end='')
    help(com)
    print(c[0], end='')
    sleep(1)


def titulo(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}  ')
    print('~' * tam)
    print(c[0], end='')
    sleep(0.6)

comando = ''
while True:
    titulo('SISTEMA DE AJUDA PYHELP', 2)
    comando = str(input('Função ou Biblioteca >'))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
titulo('Até logo!', 1)