def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\33[1:31mErro digite um número inteiro válido!\33[m')
            continue
        except KeyboardInterrupt:
            print('\n\33[1:31mO usuário preferiu não digitar esse número!\33[m')
            return 0
        else:
            return n


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\33[1:31mErro digite um número real válido!\33[m')
            continue
        except KeyboardInterrupt:
            print('\n\33[1:31mO usuário preferiu não digitar esse número\33[m!')
            return 0
        else:
            return n


inteiro = leiaInt('Digite um número inteiro:')
real = leiaFloat('Digite um número real:')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}!')

