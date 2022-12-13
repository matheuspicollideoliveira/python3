soma = 0
maioridadedehomem = 0
veterano = 0
cont = 0
for c in range(1, 5):
    nome = str(input(f'Nome da {c}ª pessoa:')).strip()
    idade = int(input(f'Idade da {c}ª pessoa:'))
    sexo = str(input(f'Sexo da {c}ª pessoa (F ou M):')).strip()
    print(30 * '-')
    soma += idade
    if c == 1 and sexo in 'Mm':
        maioridadedehomem = idade
        veterano = nome
    if sexo in 'Mm' and idade > maioridadedehomem:
        maioridadedehomem = idade
        veterano = nome
    if idade < 20 and sexo in 'Ff':
        cont += 1
media = soma / 4
print(f'O homem mais velho tem {maioridadedehomem} anos e se chama {veterano}! ')
print(f'A média de idade do grupo é de {media} anos!')
print(f'Exitem {cont} mulheres com menos de 20 anos!')

