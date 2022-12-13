import math
v = int(input('Velocidade do carro em km/h:'))
m = (v - 80) * 7
if v > 80:
    print(f'MULTADO,você excedeu o limite de velocidade que é de 80km/h, a multa irá custar R${math.trunc(m):.2f}!')
else:
    print('Tenha um bom dia, dirija com segurança!')
