from time import sleep


def maior(* num):
    tot = maior = 0
    print(25 * '-=')
    print('Analisando os valores passados...')
    for c in range(0, len(num)):
        print(num[c], end=' ')
        sleep(0.3)
        tot += 1
        if c == 0:
            maior = num[c]
        else:
            if num[c] > maior:
                maior = num[c]
    print()
    print(f'Foram analisados {tot} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(1, 2)
maior(1, 2, 5, 7)
maior(2, 9, 4, 5, 7, 1)
