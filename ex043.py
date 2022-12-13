peso = float(input('Digite seu peso em Kg:'))
altura = float(input('Digite sua altura em metros:'))
imc = peso / (altura ** 2)
if imc < 18.5:
    print(f'Seu IMC é {imc:.2f} e você está \33[31mabaixo do peso!\33[m')
elif 18.5 <= imc < 25:
    print(f'Seu IMC é {imc:.2f} e você está no \33[1:32mpeso ideal!\33[m')
elif 25 <= imc < 30:
    print(f'Seu IMC é {imc:.2f} e você está com \33[33msobrepeso!\33[m')
elif 30 <= imc < 40:
    print(f'Seu IMC é {imc:.2f} e você está com \33[34mobesidade\33[m!')
elif imc >= 40:
    print(f'Seu IMC é {imc:.2f} e você está com \33[1:31mobesidade morbida!\33[m')
