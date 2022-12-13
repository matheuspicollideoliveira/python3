from math import sin, cos, tan, trunc, radians
ângulo = float(input('Digite o ângulo que deseja:'))
seno = sin(radians(ângulo))
cosseno = cos(radians(ângulo))
tangente = tan(radians(ângulo))
print(f'O ângulo de {trunc(ângulo)}° tem o SENO de {(seno):.2f}!')
print(f'O ângulo de {trunc(ângulo)}° tem o COSSENO de {(cosseno):.2f}!')
print(f'O ângulo de {trunc(ângulo)}° tem o TANGENTE de {(tangente):.2f}!')