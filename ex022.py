nome = str(input('Digite o nome completo:')).strip()
divido = nome.split()
print(f'Seu nome em maiúsculas é {nome.upper()}!')
print(f'Seu nome em minúsculas é {nome.lower()}')
print(f'Seu nome sem espaços tem {len(nome) - nome.count(" ")} letras!')
print(f'Seu primeiro nome é {divido[0]} e ele tem {len(divido[0])} letras!')