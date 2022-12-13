def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError,TypeError):
            print('\33[1:31mErro digite um número real válido!\33[m')
            continue
        except KeyboardInterrupt:
            print('\n\33[1:31mO usuário preferiu não digitar esse número\33[m!')
            return 0
        else:
            return n


def linha(tam=42):
    return '-'*tam


def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    for c, v in enumerate(lista):
        print(f'\33[33m{c+1}\33[m - \33[34m{v}\33[m')
    print(linha())
    opc = leiaInt('\33[35mSua opçao:\33[m')
    return opc
